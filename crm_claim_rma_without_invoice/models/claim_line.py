# -*- coding: utf-8 -*-
##############################################################################
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models, api, exceptions
from openerp.addons.crm_claim_rma.models.invoice_no_date import InvoiceNoDate
from openerp.addons.crm_claim_rma.models.product_no_supplier \
    import ProductNoSupplier
from datetime import datetime
from openerp.tools import (DEFAULT_SERVER_DATE_FORMAT,
                           DEFAULT_SERVER_DATETIME_FORMAT)


class ClaimLine(models.Model):
    _inherit = "claim.line"

    prodlot_id = fields.Many2one(domain="[('product_id', '=', product_id)]")
    product_returned_quantity = fields.Float(default=1)

    @api.onchange('product_id')
    @api.depends('product_id.list_price')
    def _onchange_product_id(self):
        """
        Load list_price from product information
        """
        if self.product_id:
            self.unit_sale_price = self.product_id.list_price

    @api.onchange('product_returned_quantity', 'unit_sale_price')
    def _onchange_price_quantity(self):
        """
        Load list_price from product information
        """
        self.return_value = \
            self.product_returned_quantity * self.unit_sale_price

    def _warranty_limit_values(self, invoice, claim_type, product, claim_date):
        """
        Override _warranty_limit_values to avoid checking invoice
        """
        # We don't have inovice as a requirement anymore.
        if not (claim_type and product and claim_date):
            return {'guarantee_limit': False, 'warning': False}

        if invoice:
            invoice_date = invoice.create_date
            # We have an invoice but can't retrieve the date
            if not invoice_date:
                raise InvoiceNoDate
        else:
            invoice_date = datetime.strptime(
                datetime.now().date(),
                DEFAULT_SERVER_DATETIME_FORMAT)
        warning = 'not_define'
        invoice_date = datetime.strptime(invoice_date,
                                         DEFAULT_SERVER_DATETIME_FORMAT)

        if isinstance(claim_type, self.env['crm.claim.type'].__class__):
            claim_type = claim_type.id

        if claim_type == self.env.ref('crm_claim_type.'
                                      'crm_claim_type_supplier').id:
            try:
                warranty_duration = product.seller_ids[0].warranty_duration
            except IndexError:
                raise ProductNoSupplier
        else:
            warranty_duration = product.warranty

        limit = self.warranty_limit(invoice_date, warranty_duration)
        if warranty_duration > 0:
            claim_date = datetime.strptime(claim_date,
                                           DEFAULT_SERVER_DATETIME_FORMAT)
            if limit < claim_date:
                warning = 'expired'
            else:
                warning = 'valid'

        return {'guarantee_limit': limit.strftime(DEFAULT_SERVER_DATE_FORMAT),
                'warning': warning}

    def set_warranty_limit(self):
        self.ensure_one()

        claim = self.claim_id
        invoice_id = self.invoice_line_id and self.invoice_line_id.invoice_id \
            or claim.invoice_id
        try:
            values = self._warranty_limit_values(
                invoice_id, claim.claim_type,
                self.product_id, claim.date)
        except InvoiceNoDate:
            raise exceptions.Warning(
                _('Error'), _('Cannot find any date for invoice. '
                              'Must be a validated invoice.'))
        except ProductNoSupplier:
            raise exceptions.Warning(
                _('Error'), _('The product has no supplier configured.'))

        self.write(values)
        return True

    @api.multi
    def set_warranty(self):
        """
        Calculate warranty limit and address
        """
        for line_id in self:
            if not line_id.product_id:
                raise exceptions.Warning(
                    _('Error'), _('Please set product first'))

            line_id.set_warranty_limit()
            line_id.set_warranty_return_address()

    @api.model
    def create(self, vals):
        """
        Set default destination location in case it is not defined
        """
        if ('location_dest_id' not in vals) and ('product_id' in vals) and (
                'claim_id' in vals):
            claim = self.env['crm.claim'].browse([vals.get('claim_id')])
            product = self.env['product.product'].browse(
                [vals.get('product_id')])
            location_dest_id = self.get_destination_location(
                product,
                claim.warehouse_id)
            vals.update(
                {'location_dest_id': location_dest_id.id}
            )
        res = super(ClaimLine, self).create(vals)
        return res

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

from openerp import fields, models, api


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


    @api.onchange('product_returned_quantity','unit_sale_price')
    def _onchange_price_quantity(self):
        """
        Load list_price from product information
        """
        self.return_value = self.product_returned_quantity * self.unit_sale_price

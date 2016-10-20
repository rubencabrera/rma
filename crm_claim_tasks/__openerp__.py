# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2016 Praxya
#    Author: Rubén Cabrera Martínez
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

{
    'name': 'RMA Tasks',
    'version': '8.0.0.1',
    'category': 'Generic Modules/CRM & SRM',
    'author': "Rubén Cabrera, Praxya, "
              "Odoo Community Association (OCA)",
    'website': 'http://www.praxya.com',
    'license': 'AGPL-3',
    'depends': [
        'project_task_materials_stock',
        'crm_claim_rma',
    ],
    'data': [
        # 'data/ir_sequence_type.xml',
        'data/project_task_type.xml',
        # 'data/crm_case_categ.xml',
        # 'views/account_invoice.xml',
        # 'wizards/claim_make_picking.xml',
        'views/crm_claim.xml',
        # "views/claim_line.xml",
        # 'views/res_partner.xml',
        # 'views/stock_view.xml',
        # 'security/ir.model.access.csv',
    ],
    'demo': [
        # 'demo/account_invoice.xml',
        # 'demo/account_invoice_line.xml',
        # 'demo/crm_claim.xml',
        # TODO: Create sample task
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}

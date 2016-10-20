# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2016 Praxya
#    Author: Rubén Cabrera Martínez, Praxya
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
from openerp import _, fields, models


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    task_ids = fields.One2many('project.task', 'claim_id', string=_('Tasks'),
                               copy=False, help=_("Tasks to carry out to solve "
                                                  "this claim"))

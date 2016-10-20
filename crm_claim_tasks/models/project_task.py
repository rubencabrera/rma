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
# ##############################################################################

from openerp import _, fields, models, api
import logging

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = "project.task"

    claim_id = fields.Many2one('crm.claim', string=_('Claim'))

    # @api.model
    # def create(self, values):
        # """
        # Check for outgoing pickings in the RMA to check if any materials
        # are to be added to the task.
        # """
        # if values.get('claim_id', False) is not False:
            # # If there's a claim, get its pickings and check their type
            # claim = self.env['crm.claim'].browse(values.get('claim_id'))
            # if claim.picking_ids is not False and claim.picking_ids != []:
                # for picking in claim.picking_ids:
                    # if picking.picking_type_id == self.env.ref(
                                    # 'stock.picking_type_out').id:
                        # moves = self.env['stock.move']
                        # for move in picking.move_lines:
                            # moves |= move
                        # _logger.debug('Moves: {0}'.format(moves))
        # res = super(ProjectTask, self).create(values)
        # return res

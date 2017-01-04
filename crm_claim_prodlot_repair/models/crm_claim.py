# -*- coding: utf-8 -*-
# Copyright Copyright 2016 Rubén Cabrera Martínez, Praxya Soluciones
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models, api


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    @api.one
    def create_repair_tasks(self):
        """
        Create tasks
        """
        task_obj = self.env['project.task']
        # Claim lines with related serials
        for line in self.claim_line_ids.filtered('prodlot_id'):
            task_obj.create({
                'name': self.code + ' ' + line.prodlot_id.name,
                'reviewer_id': self.env.user.id,
                'priority': self.priority,
                'date_deadline': self.date_deadline,
                'date_start': fields.datetime.now(),
                'claim_id': self.id,
            })

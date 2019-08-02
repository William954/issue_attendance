# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    user_logged_id = fields.Many2one('res.users', string='Solicitante', default=lambda self: self.env.user, track_visibility=True)
    logged_id = fields.Boolean(string='No approval user logged', compute="_active_id")

    @api.depends('user_logged_id','logged_id')
    def _active_id(self):
        if self.env.user.employee_ids.id == self.employee_id:
            self.logged_id = True
        else:
            self.logged_id = False

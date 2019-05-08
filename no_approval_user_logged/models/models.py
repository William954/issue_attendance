# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    user_logged_id = fields.Many2one('res.user', string='Solicitante', default=lambda self: self.env.user, track_visibility=True)
    logged_id = fields.Boolean(string='No approval user logged',compute="_active_id")

    @api.depends('logged_jd')
    def _active_id(self):
        if self.env.user == self.logged_id:
            self.logged_jd = True
        else:
            self.logged_jd = False

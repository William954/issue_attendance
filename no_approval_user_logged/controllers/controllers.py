# -*- coding: utf-8 -*-
from odoo import http

# class NoApprovalUserLogged(http.Controller):
#     @http.route('/no_approval_user_logged/no_approval_user_logged/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/no_approval_user_logged/no_approval_user_logged/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('no_approval_user_logged.listing', {
#             'root': '/no_approval_user_logged/no_approval_user_logged',
#             'objects': http.request.env['no_approval_user_logged.no_approval_user_logged'].search([]),
#         })

#     @http.route('/no_approval_user_logged/no_approval_user_logged/objects/<model("no_approval_user_logged.no_approval_user_logged"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('no_approval_user_logged.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
# from odoo import http


# class /home/odoo/src/user/(http.Controller):
#     @http.route('//home/odoo/src/user///home/odoo/src/user//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/odoo/src/user///home/odoo/src/user//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/odoo/src/user/.listing', {
#             'root': '//home/odoo/src/user///home/odoo/src/user/',
#             'objects': http.request.env['/home/odoo/src/user/./home/odoo/src/user/'].search([]),
#         })

#     @http.route('//home/odoo/src/user///home/odoo/src/user//objects/<model("/home/odoo/src/user/./home/odoo/src/user/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/odoo/src/user/.object', {
#             'object': obj
#         })

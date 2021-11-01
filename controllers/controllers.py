# -*- coding: utf-8 -*-
# from odoo import http


# class Takslaundry(http.Controller):
#     @http.route('/takslaundry/takslaundry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/takslaundry/takslaundry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('takslaundry.listing', {
#             'root': '/takslaundry/takslaundry',
#             'objects': http.request.env['takslaundry.takslaundry'].search([]),
#         })

#     @http.route('/takslaundry/takslaundry/objects/<model("takslaundry.takslaundry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('takslaundry.object', {
#             'object': obj
#         })

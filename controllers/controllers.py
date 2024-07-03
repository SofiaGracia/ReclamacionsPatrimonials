# -*- coding: utf-8 -*-
# from odoo import http


# class Rp(http.Controller):
#     @http.route('/rp/rp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rp/rp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rp.listing', {
#             'root': '/rp/rp',
#             'objects': http.request.env['rp.rp'].search([]),
#         })

#     @http.route('/rp/rp/objects/<model("rp.rp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rp.object', {
#             'object': obj
#         })

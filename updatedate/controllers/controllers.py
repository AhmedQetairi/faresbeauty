# -*- coding: utf-8 -*-
# from odoo import http


# class Updatedate(http.Controller):
#     @http.route('/updatedate/updatedate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/updatedate/updatedate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('updatedate.listing', {
#             'root': '/updatedate/updatedate',
#             'objects': http.request.env['updatedate.updatedate'].search([]),
#         })

#     @http.route('/updatedate/updatedate/objects/<model("updatedate.updatedate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('updatedate.object', {
#             'object': obj
#         })

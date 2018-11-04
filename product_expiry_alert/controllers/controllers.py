# -*- coding: utf-8 -*-
from odoo import http

# class ProductExpiryAlert(http.Controller):
#     @http.route('/product_expiry_alert/product_expiry_alert/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_expiry_alert/product_expiry_alert/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_expiry_alert.listing', {
#             'root': '/product_expiry_alert/product_expiry_alert',
#             'objects': http.request.env['product_expiry_alert.product_expiry_alert'].search([]),
#         })

#     @http.route('/product_expiry_alert/product_expiry_alert/objects/<model("product_expiry_alert.product_expiry_alert"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_expiry_alert.object', {
#             'object': obj
#         })
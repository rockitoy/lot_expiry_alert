# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    removal_date = fields.Date(related='lot_id.removal_date', store=True)


class product_expiry_alert(models.Model):
    _inherit = 'stock.production.lot'

    life_date = fields.Date(string='End of Life Date', related='removal_date',
        help='This is the date on which the goods with this Serial Number may become dangerous and must not be consumed.')
    use_date = fields.Date(string='Best before Date', related='removal_date',
        help='This is the date on which the goods with this Serial Number start deteriorating, without being dangerous yet.')
    removal_date = fields.Date(string='Removal Date',
        help='This is the date on which the goods with this Serial Number should be removed from the stock.')
    alert_date = fields.Date(string='Alert Date',
        help="This is the date on which an alert should be notified about the goods with this Serial Number.")
    user_id =fields.Many2one('res.users','Responsible',default=lambda self:self.env.user )
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env['res.company']._company_default_get('stock.production.lot'))


    @api.multi
    def alert_product_expiry(self):
        # print'product_qty',self.product_qty
        alert_data = self.search([('alert_date','=',fields.Date.today())])
        if alert_data :
            for expiry_data_id in alert_data:
                if expiry_data_id.product_qty > 0:
                    total_qty = 0.0
                    params = [expiry_data_id.id]
                    query = """ SELECT sl.name as location,sum(quantity) as qty from stock_quant sq
                    JOIN stock_location sl ON sl.id = sq.location_id
                    where lot_id =%s and sq.location_id in (SELECT id from stock_location
                    where usage='internal') and sq.quantity > 0
                    GROUP BY location"""
                    self.env.cr.execute(query,params)
                    data = self.env.cr.dictfetchall()
                    for re in data:
                        total_qty+=re['qty']
                    template_id = self.env.ref('product_expiry_alert.expiry_alert_email_template')
                    send = template_id.with_context(data = data,total_qty=total_qty).send_mail(expiry_data_id.id, force_send=True)


    # @api.multi
    # def _alert_product_expiry(self):
    #     alert_data = self.search([('alert_date','=',fields.Date.today())])
    #     print'alert_data',alert_data
    #     stock_quant_ids = self.env['stock.quant'].search([('lot_id','in',alert_data.ids),('quantity','>',0)],order ='product_id asc')
    #     stock_data = []
    #     # if stock_quant_ids:
    #     for res in self.env['stock.quant'].search([('lot_id','in',alert_data.ids),('quantity','>',0)],order ='product_id asc'):
    #         stock_data.append(dict(product=res.product_id.name,location=res.location_id.name,qty=res.quantity))
    #     print'stock_datastock_data',stock_data
    #     template_id = self.env.ref('product_expiry_alert.expiry_alert_email_template')
    #     send = template_id.with_context(data = stock_data).send_mail(expiry_data_id.id, force_send=True)
        # if alert_data:
        #     for expiry_data_id in alert_data:
        #         total_qty = 0.0
        #         params = [expiry_data_id.id]
        #         query = """ SELECT sl.name as location,sum(quantity) as qty from stock_quant sq
        #         JOIN stock_location sl ON sl.id = sq.location_id
        #         where lot_id =%s and sq.location_id in (SELECT id from stock_location
        #         where usage='internal') and sq.quantity > 0
        #         GROUP BY location"""
        #         self.env.cr.execute(query,params)
        #         data = self.env.cr.dictfetchall()
        #         for re in data:
        #             total_qty+=re['qty']
        #         template_id = self.env.ref('product_expiry_alert.expiry_alert_email_template')
                # send = template_id.with_context(data = data,total_qty=total_qty).send_mail(expiry_data_id.id, force_send=True)

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Management Sale Order Line View'

    partner = fields.Many2one('res.partner', related='order_id.partner_id')

    product_so_detail_ids = fields.Many2many('sale.order.line', string="Products", compute='_compute_product_so_get_detail_ids')

    def _compute_product_so_get_detail_ids(self):
        product_order = self.env['sale.order.line'].search(
            [('product_id', '=', self.product_id.id), ('order_id.state', '=', 'sale')],
            order='create_date desc', limit=5)
        self.product_so_detail_ids = product_order



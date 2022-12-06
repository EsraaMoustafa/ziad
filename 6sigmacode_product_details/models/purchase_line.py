# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseLineInherit(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Management Purchase Line View'

    product_po_detail_ids = fields.Many2many('sale.order.line', string="Products",
                                             compute='_compute_product_po_get_detail_ids')
    sale_order_line_id = fields.Many2one('sale.order.line')

    def _compute_product_po_get_detail_ids(self):
        product_order = self.env['sale.order.line'].search(
            [('product_id', '=', self.product_id.id), ('order_id.state', '=', 'sale')],
            order='create_date desc', limit=5)
        self.product_po_detail_ids = product_order

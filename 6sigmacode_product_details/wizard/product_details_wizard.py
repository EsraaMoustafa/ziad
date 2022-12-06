# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from odoo.tools.translate import _


class ProductPoDetailsWizard(models.TransientModel):
    _name = "product.po.details.wizard"
    _description = "Product Details Wizard"

    def _default_po_product_details(self):
        if self.env.context.get('active_model') == 'purchase.order.line':
            ids = self.env.context['active_ids']
            order_lines = self.env['purchase.order.line'].browse(ids)
            if order_lines:
                for line in order_lines:
                    product_po_details = line.product_po_detail_ids
                    return product_po_details

    product_po_details = fields.Many2many('sale.order.line', 'sale_order_line_id', string='Products Details',
                                          default=_default_po_product_details,
                                          required=True, readonly=True)


class ProductSoDetailsWizard(models.TransientModel):
    _name = "product.so.details.wizard"
    _description = "Product SO Details Wizard"

    def _default_so_product_details(self):
        if self.env.context.get('active_model') == 'sale.order.line':
            ids = self.env.context['active_ids']
            order_lines = self.env['sale.order.line'].browse(ids)
            if order_lines:
                for line in order_lines:
                    product_so_details = line.product_so_detail_ids
                    return product_so_details

    product_so_details = fields.Many2many('sale.order.line', string='Products Details',
                                          default=_default_so_product_details,
                                          required=True, readonly=True)

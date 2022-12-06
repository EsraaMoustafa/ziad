# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    margin_qty = fields.Float('Margin', compute="_compute_margin_amount", store=True)

    @api.depends('margin', 'standard_price', 'list_price')
    def _compute_margin_amount(self):
        for product in self:
            if product.margin and product.list_price and product.standard_price:
                product.margin_qty = product.list_price - product.standard_price

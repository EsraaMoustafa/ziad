# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Float('Disc Amount', default=0.0)

    @api.onchange('discount', 'price_unit', 'product_uom_qty')
    def onchange_so_discount_amount(self):
        if self.env.user.has_group('product.group_discount_per_so_line'):
            self.discount_amount = 0.0
            for rec in self:
                if rec.product_id and rec.discount:
                    rec.discount_amount = (rec.discount / 100) * (rec.price_unit * rec.product_uom_qty)

    @api.onchange('discount_amount', 'price_unit', 'product_uom_qty')
    def onchange_so_discount(self):
        if self.env.user.has_group('product.group_discount_per_so_line'):
            self.discount = 0.0
            for rec in self:
                if rec.product_id and rec.discount_amount:
                    rec.discount = (rec.discount_amount * 100) / (rec.price_unit * rec.product_uom_qty)


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    discount_amount = fields.Float('Disc Amount')

# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PurchaseOrderLineInherit(models.Model):
    _inherit = 'purchase.order.line'

    discount_amount = fields.Float('Disc Amount', default=0.0)

    @api.onchange('discount', 'price_unit', 'product_qty')
    def onchange_pu_discount_amount(self):
        self.discount_amount = 0.0
        for rec in self:
            if rec.product_id and rec.discount:
                rec.discount_amount = (rec.discount / 100) * (rec.price_unit * rec.product_qty)

    @api.onchange('discount_amount', 'price_unit', 'product_qty')
    def onchange_pu_discount(self):
        self.discount = 0.0
        for rec in self:
            if rec.product_id and rec.discount_amount:
                rec.discount = (rec.discount_amount * 100) / (rec.price_unit * rec.product_qty)


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    discount_amount = fields.Float('Disc Amount', compute="_compute_discount_amount", default=0.0)

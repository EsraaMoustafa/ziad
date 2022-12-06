# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Float('Disc Amount', force_save=True)

    @api.onchange('discount')
    @api.depends('discount')
    def onchange_am_discount_amount(self):
        self.discount_amount = 0.0
        for rec in self:
            if rec.product_id and rec.discount:
                rec.discount_amount = (rec.discount / 100) * (rec.price_unit * rec.quantity)

    @api.onchange('discount_amount')
    @api.depends('discount_amount')
    def onchange_am_discount(self):
        self.discount = 0.0
        for rec in self:
            if rec.product_id and rec.discount_amount:
                rec.discount = (rec.discount_amount * 100) / (rec.price_unit * rec.quantity)


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    discount_amount = fields.Float('Disc Amount', default=0.0)

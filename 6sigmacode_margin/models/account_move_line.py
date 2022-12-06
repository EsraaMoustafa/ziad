# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    unit_margin = fields.Float('Unit Margin', compute="_compute_unit_margin", store=True)
    margin_percent = fields.Float('Margin %', compute="_compute_margin_percent", store=True)
    total_cost = fields.Float('Total Cost', compute="_compute_total_cost", store=True)
    unit_cost = fields.Float('Unit Cost', compute="_compute_unit_cost", store=True)
    total_price = fields.Float('Total Price', compute="_compute_total_price", store=True)

    @api.depends('quantity', 'line_margin')
    @api.onchange('quantity', 'line_margin')
    def _compute_unit_margin(self):
        for rec in self:
            if rec.quantity and rec.line_margin:
                rec.unit_margin = rec.line_margin / rec.quantity

    @api.depends('price_subtotal', 'line_margin')
    def _compute_total_cost(self):
        for rec in self:
            if rec.price_subtotal and rec.line_margin:
                rec.total_cost = rec.price_subtotal - rec.line_margin

    @api.depends('total_cost')
    def _compute_unit_cost(self):
        for rec in self:
            if rec.total_cost and rec.quantity:
                rec.unit_cost = rec.total_cost / rec.quantity

    @api.depends('line_margin', 'total_cost')
    @api.onchange('line_margin', 'total_cost')
    def _compute_margin_percent(self):
        for rec in self:
            if rec.line_margin and rec.total_cost:
                rec.margin_percent = (rec.line_margin * 100) / rec.total_cost

    @api.depends('quantity', 'price_unit')
    @api.onchange('quantity', 'price_unit')
    def _compute_total_price(self):
        for rec in self:
            if rec.quantity and rec.price_unit:
                rec.total_price = rec.quantity * rec.price_unit

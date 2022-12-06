# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrderMinAndMuxPrice(models.Model):
    _inherit = 'sale.order'


class SaleOrderLineMinAndMuxPrice(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Add Minimum And Muximum Price fields In Line'

    min_sale_price = fields.Float(string="Minimum Sale Price", related="product_id.min_sale_price")
    max_sale_price = fields.Float(string="maximum Sale Price", related="product_id.max_sale_price")

    @api.model
    @api.depends('min_sale_price', 'max_sale_price')
    @api.constrains('price_unit')
    def constraint_unit_price(self):
        user = self.env.user
        for record in self:
            if user.has_group('6SigmaCode_Minimum_Maximum_Price.group_minimum_maximum_sale_price'):
                if record.price_unit > record.max_sale_price:
                    raise ValidationError(_("Unit Price Should Be Between Minimum Price And Maximum Price"))
                if record.price_unit < record.min_sale_price:
                    raise ValidationError(_("Unit Price Less Than Minimum Price"))
            else:
                pass

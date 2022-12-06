# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductVariantsMinAndMuxPrice(models.Model):
    _inherit = 'product.template'
    _description = 'Managment Minimum And Muximum Price'

    min_sale_price = fields.Float(string="Minimum Sale Price", groups="6SigmaCode_Minimum_Maximum_Price.group_minimum_maximum_sale_price")
    max_sale_price = fields.Float(string="maximum Sale Price", groups="6SigmaCode_Minimum_Maximum_Price.group_minimum_maximum_sale_price")



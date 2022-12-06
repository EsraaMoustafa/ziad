# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError


class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    order_line_id = fields.Many2one('sale.order.line')

    @api.constrains('product_id')
    def action_confirm(self):
        res = super(SaleOrderInherit, self).action_confirm()
        user = self.env.user
        for rec in self.order_line:
            if rec.margin < 0:
                if user.has_group('6sigmacode_product_confirm_restrictions.group_not_confirm_sale_order_product'):
                    return res
                else:
                    raise ValidationError(_('غير مسموح البيع  لمنتج باقل من سعر التكلفة برجاء مراجعة مدير المبيعات او المحاسب بالنسبة " %s " ' % rec.product_id.name))

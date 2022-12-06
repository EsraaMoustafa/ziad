# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import ValidationError


class AccountMoveInherit(models.Model):
    _inherit = "account.move"

    account_move_id = fields.Many2one('account.move.line')

    @api.constrains('product_id')
    def action_post(self):
        res = super(AccountMoveInherit, self).action_post()
        user = self.env.user
        if self.move_type == 'out_invoice':
            for rec in self.invoice_line_ids:
                if rec.line_margin < 0:
                    if user.has_group('6sigmacode_product_confirm_restrictions.group_not_confirm_account_move_product'):
                        return res
                    else:
                        raise ValidationError(_('غير مسموح البيع  لمنتج باقل من سعر التكلفة برجاء مراجعة مدير المبيعات او المحاسب بالنسبة " %s " ' % rec.product_id.name))

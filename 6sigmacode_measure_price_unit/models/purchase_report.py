# -*- coding: utf-8 -*-

from odoo import exceptions, models, api, fields, _


class PurchaseReportInherit(models.Model):
    _inherit = 'purchase.report'

    price_unit = fields.Float(String="Price Unit")

    def _select(self):
        return super(PurchaseReportInherit, self)._select() + ", price_unit as price_unit"

    # def _from(self):
    #     return super(PurchaseReportInherit, self)._from() + " join price_unit  on (price_unit=l.price_unit)"
    #
    def _group_by(self):
        return super(PurchaseReportInherit, self)._group_by() + ", price_unit"

# -*- coding: utf-8 -*-

from odoo import exceptions, models, api, fields, _


class SaleReportInherit(models.Model):
    _inherit = 'sale.report'

    line_margin = fields.Float(String="Margin")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['margin'] = ", l.margin"
        groupby += ', l.margin'
        res = super(SaleReportInherit, self)._query(with_clause, fields, groupby, from_clause)
        return res



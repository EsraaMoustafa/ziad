# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.
import logging
from odoo import api, fields, models, _, tools

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning("The num2words python library is not installed, amount-to-text features won't be fully available.")
    num2words = None


class Company(models.Model):
    _inherit = "res.company"

    qr_code_generation_config = fields.Selection([
        ('auto', 'Generate QR Code when Invoice validate/post'),
        ('manual', 'Manually Generate')], string="QR Code Generation Configuration",
        default='auto')
    bank_name = fields.Char("Bank Name")
    ibn = fields.Char("IBAN")
    vat_reports = fields.Selection([
        ('report1', 'Simplified Tax Invoice Type 1'),
        ('report1_1', 'Simplified Tax Invoice Type 1_1'),
        ('report2', 'Simplified Tax Invoice Type 2'),
        ('report3', 'Simplified Tax Invoice Type 3'),
        ('report4', 'Simplified Tax Invoice Type 4'),
        ('report5', 'VAT Invoice'),
    ], 'Type Of Vat Report')
    approved_by = fields.Char('Report Approved By')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    qr_code_generation_config = fields.Selection(string="QR Code Generation Configuration",
                                                 related="company_id.qr_code_generation_config", readonly=False)


class Currency(models.Model):
    _inherit = 'res.currency'

    def amount_to_text(self, amount):
        self.ensure_one()

        def _num2words(number, lang):
            try:
                return num2words(number, lang=lang).title()
            except NotImplementedError:
                return num2words(number, lang='en').title()

        if num2words is None:
            logging.getLogger(__name__).warning("The library 'num2words' is missing, cannot render textual amounts.")
            return ""

        formatted = "%.{0}f".format(self.decimal_places) % amount
        parts = formatted.partition('.')
        integer_value = int(parts[0])
        fractional_value = int(parts[2] or 0)

        lang_code = self.env.context.get('lang') or self.env.user.lang
        lang = tools.get_lang(self.env)
        if lang_code == 'ar_001':
            amount_words = tools.ustr('{amt_value} {amt_word}').format(
                amt_value=_num2words(integer_value, lang=lang.iso_code),
                amt_word='ريال',
            )
            if not self.is_zero(amount - integer_value):
                amount_words += ' ' + _('و') + tools.ustr('{amt_value} {amt_word}').format(
                    amt_value=_num2words(fractional_value, lang=lang.iso_code),
                    amt_word='هللة',
                )
        else:
            amount_words = tools.ustr('{amt_value} {amt_word}').format(
                amt_value=_num2words(integer_value, lang=lang.iso_code),
                amt_word=self.currency_unit_label,
            )
            if not self.is_zero(amount - integer_value):
                amount_words += ' ' + _('and') + tools.ustr(' {amt_value} {amt_word}').format(
                    amt_value=_num2words(fractional_value, lang=lang.iso_code),
                    amt_word=self.currency_subunit_label,
                )
        return amount_words

    def invoice_amount_in_words(self, lang, amount):
        return self.currency_id.with_context(lang=lang).amount_to_text(amount)

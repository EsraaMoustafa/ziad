# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'
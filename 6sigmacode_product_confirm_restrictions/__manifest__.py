# -*- coding: utf-8 -*-
{
    'name': "Product Cost Confirm",
    'author': 'Ascetic Business Solution',
    'category': 'Accounting',
    'summary': """Product Cant Confirmed In sale Order If Product Cost In Sale Order Line Greater Than The Cost In Product Template""",
    'website': 'http://www.6sigmacode.com',
    'description': """Product Cant Confirmed In sale Order If Product Cost In Sale Order Line Greater Than The Cost In Product Template""",
    'version': '14.0.1.0',
    'depends': ['base', 'sale_management', 'account', 'ob_invoice_line_view'],
    'data': [
        'security/security.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}

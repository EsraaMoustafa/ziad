# -*- coding: utf-8 -*-
{
    'name': '6sigmaCode Margin',
    'version': '14.1',
    'author': "6Sigma Code",
    'summary': 'Product Margin',
    'description': """Product Margin""",
    'category': 'account',
    'depends': ['margin', 'account', 'ob_invoice_line_view', '6sigmacode_discount_amount'],
    'data': [
        'views/account_move_line_view.xml',
        'views/product_template_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

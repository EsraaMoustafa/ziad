 # -*- coding: utf-8 -*-
{
    'name': "6Sigmacode States Security",

    'summary': """Add Security At reset to draft, cancel and confirm Buttons In Sale Order Module And Account Move""",

    'description': """Add Security At reset to draft, cancel and confirm Buttons In Sale Order Module And Account Move""",
    'author': "6sigmacode",
    'website': "",
    'category': 'Accounting',
    'version': '14.0.0.0',
    'depends': ['base', 'sale_management', 'account'],
    'qweb': [],
    'data': [
        'security/security.xml',
        'view/account_move_view.xml',
        'view/sale_order_view.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': False,
    'installable': True,
}
 # -*- coding: utf-8 -*-
{
    'name': "Discount Amount",

    'summary': """Compute Discount in Sale Order Line Purchase Order Line Account Move Line""",

    'description': """Compute Discount in Sale Order Line Purchase Order Line Account Move Line""",
    'author': "6sigmacode",
    'website': "",
    'category': 'Accounting',
    'version': '14.0.0.0',
    'depends': ['base', 'sale_management', 'account', 'purchase', 'purchase_discount',],
    'qweb': [],
    'data': [
        'security/ir.model.access.csv',
        'view/account_move_view.xml',
        'view/purchase_view.xml',
        'view/sale_order_view.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': False,
    'installable': True,
}
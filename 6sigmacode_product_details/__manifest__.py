 # -*- coding: utf-8 -*-
{
    'name': "Product Details Icon",

    'summary': """Add Icon In Sale Order Line And Purchase Line To Popup Last 5 Orders Of This Product""",

    'description': """Add Icon In Sale Order Line And Purchase Line To Popup Last 5 Orders Of This Product""",
    'author': "6sigmacode",
    'website': "",
    'category': 'Sale',
    'version': '14.0.0.0',
    'depends': ['base', 'sale_management', 'purchase'],
    'qweb': [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_po_details_wizard_view.xml',
        'wizard/product_so_details_wizard_view.xml',
        'views/purchase_order_view.xml',
        'views/sale_order_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': False,
    'installable': True,
}
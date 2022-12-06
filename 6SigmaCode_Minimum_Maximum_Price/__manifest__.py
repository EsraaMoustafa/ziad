# -*- coding: utf-8 -*-
{
    'name': "Managment Minimum And Muximum Price",

    'summary': """Managment Minimum And Muximum Price In Product Variants""",

    'description': """
        Managment Minimum And Muximum Price In Product Variants And Add Security At Fields Of Minimum And Muximum
    """,
    'author': "6SigmaCode Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale'],
    'data': [
        'security/security.xml',
        'views/product_variants_view.xml',
        'views/sale_order_view.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

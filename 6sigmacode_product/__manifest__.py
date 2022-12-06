# -*- coding: utf-8 -*-
{
    'name': "Managment Product Security",

    'summary': """Management Product Security""",

    'description': """
        Management Product Security to hide cost field for user and hide vendors menuitem also 
    """,

    'author': "6SigmaCode Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/product_template_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}

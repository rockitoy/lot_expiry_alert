# -*- coding: utf-8 -*-
{
    'name': "Produt Expiry Alert",

    'summary': """
        Send alert mail to responsible person based on product expiry""",

    'description': """

    """,

    'author': "KABEER KB",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'price':10,
    'currency':'EUR',
    'license': 'OPL-1',
    'category': 'Product',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','product_expiry'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable':True,
}

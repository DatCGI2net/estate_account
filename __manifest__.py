# -*- coding: utf-8 -*-
{
    'name': "Estate Account Pilot",

    'summary': """
        An realestate account advertisement""",

    'description': """
        Estate account
    """,

    'author': "Hip Dev",
    'website': "http://www.cgito.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/CRM',
    'version': '16.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'realestate',
        'account',

    ],
    'data': [

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
    'license': 'LGPL-3',

}

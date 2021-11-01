# -*- coding: utf-8 -*-
{
    'name': "Sewa PS Ridho",

    'summary': """
        Sewa PS Software""",

    'description': """
        Ini Sewa PS
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ridhops_view.xml',
        'views/templates.xml',
        'views/ridhops.xml',
        'views/ridhops_perawatan.xml',
        'views/ridhops_pegawai.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

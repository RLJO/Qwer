# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Cubic ERP - Teradata SAC. (https://cubicerp.com).

{
    "name": "Hammam - Accounting",
    "version": "2.0",
    "description": """
Bolivian accounting chart and tax localization.

Plan contable boliviano e impuestos de acuerdo a disposiciones vigentes

    """,
    "author": "Hemo",
    'category': 'Accounting/Localizations/Account Charts',
    "depends": ["account"],
    "data": [
        "data/account_jo_coa_data.xml",
        "data/account.account.template.csv",
        "data/account_tax_template_data.xml",
        'data/account.group.csv',
        'data/account_chart_template_data.xml',
        "data/account_data.xml",
        "data/fiscal_templates_data.xml",
        "data/res.lang.csv",
        ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}

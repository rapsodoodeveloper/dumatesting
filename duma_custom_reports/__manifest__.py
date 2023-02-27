# Copyright 2023-TODAY Rapsodoo Iberia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': 'Duma Custom Reports',
    'summary': 'Custom reports to Duma.',
    'version': '16.0.1.0.0',
    'depends': ['base', 'web', 'purchase', 'sale_management'],
    'category': 'Extra Tools',
    'author': 'Aselcis Consulting',
    'website': 'https://www.aselcis.com',
    'description': """
Implements DUMA style to:
* Request for Quotation / Purchase order
* Quotation / Sale order
    """,
    'data': [
        # 'views/assets.xml',
        'views/purchase_views.xml',
        'views/report_paperformat.xml',
        'views/report_templates.xml',
        'report/purchase_reports.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_quotation_templates.xml',
        'report/sale_report.xml',
        'report/sale_report_templates.xml'
    ],
    'assets': {
            'web.report_assets_common': [
                'duma_custom_reports/static/src/**/*',
            ],
        },
    'installable': True,
}

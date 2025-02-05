# -*- coding: utf-8 -*-
{
    'name': "purchase_approval",
    'summary': "Add approval workflow for purchase orders",
    'description': """
                    Add approval workflow for purchase orders, product API & reports
                    """,
    'author': "AMB",
    'category': 'Purchase',
    'version': '0.1',
    'depends': ['base','purchase',],
    'data': [
        # 'security/ir.model.access.csv',
        "views/purchase_order_views.xml",
        
    ],
    'external_dependencies': {'python': []},
    'installable': True,
    'application': True,
}


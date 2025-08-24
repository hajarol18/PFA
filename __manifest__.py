{
    'name': 'Smart Agri Decision',
    'version': '1.0',
    'depends': ['base', 'stock', 'product', 'project'],
    'author': 'Hajar',
    'category': 'Agriculture',
    'description': 'Module d’aide à la décision agricole basé sur les paiements géographiques',
    'data': [
    'security/ir.model.access.csv',
    'views/exploitation_views.xml',
    'views/culture_views.xml',
    'views/parcelle_views.xml',
    'views/intervention_views.xml',
    'views/intrants_views.xml',
    'views/main_menu.xml',
    'views/ai_views.xml',
    'data/demo_data.xml',
    'data/ia_demo_data.xml',
    ],

    'installable': True,
    'application': True,
}

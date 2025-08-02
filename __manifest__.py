{
    'name': 'Smart Agri Decision',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Hajar',
    'category': 'Agriculture',
    'description': 'Module d’aide à la décision agricole basé sur les paiements géographiques',
    'data': [
    'security/ir.model.access.csv',
    'views/exploitation_views.xml',
    'views/culture_views.xml',
    'views/main_menu.xml',
    'data/demo_data.xml',
    ],

    'installable': True,
    'application': True,
}

{
    'name': 'Product Composition',
    'version': '18.0.1.0.0',
    'summary': 'Manage product compositions',
    'description': 'Manage the composition of products with percentage and description.',
    'category': 'Product',
    'author': 'Codex',
    'license': 'LGPL-3',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_composition_description_views.xml',
        'views/product_composition_menu.xml',
        'views/product_composition_views.xml',
    ],
    'installable': True,
}

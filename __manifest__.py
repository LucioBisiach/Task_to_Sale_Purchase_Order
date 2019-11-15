{
    'name': 'Task to Sale/Purchase Order',
    'version': '11.0',
    'category': 'Project',
    'summary': 'Create Sale/Purchase Order from Task for Project',
    'description': """
        This module allows you to create sales or purchase orders, assigning a particular customer or supplier
    """,
    'sequence': 1,
    'author': 'Bisiach Lucio',
    'website': '',
    'depends': ['base', 'project', 'sale_management', 'purchase'],
    'data': [
        'views/project_view.xml',
        'views/sale_view.xml',
        'views/purchase_view.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/Banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 10.00,
    'currency': 'EUR'
}

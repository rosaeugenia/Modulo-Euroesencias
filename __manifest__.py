{
    'name': 'Custom Products',
    'version': '1.0',
    'description': 'Description',
    'category': 'General',
    'author': 'Na Solutions',
    'website': 'www.nasolutions.mx',
    'depends': ['base', 'product'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "security/ir_model_access.xml",
        'views/views.xml'
    ],
    'installable': True,
    'auto_install': False
}

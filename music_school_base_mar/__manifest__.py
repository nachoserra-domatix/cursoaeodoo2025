{
    'name': 'Music School Base Mar',
    'version': '1.0',
    'summary': 'Módulo base para gestionar estudiantes de una escuela de música',
    'description': """
Módulo inicial para gestionar estudiantes de una escuela de música.
Incluye modelo básico, vistas, menú y permisos.
    """,
    'author': 'Mar',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/music_school_base_student_views.xml',
        'views/music_school_base_instrument_views.xml',
        'views/music_school_base_menuitems.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

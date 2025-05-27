{
    'name': 'Music School',
    'version': '1.0',
    'description': 'Module for music school',
    'summary': 'Music School Management',
    'category': 'Education',
    'author': 'Edu',
    'installable': True,
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'views/music_school_student_view.xml',
        'views/music_school_instrument_view.xml',
        'views/music_school_menuitems.xml',
    ],
    'auto_install': False,
    'application': False,
}
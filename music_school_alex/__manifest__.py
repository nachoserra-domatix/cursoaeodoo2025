{
    'name' : 'Music School',
    'version': '18.0.0.0.0',
    'description': 'Manages a music school with students, teacher, and classes',
    'summary': 'Manages a music school with students, teacher, and classes',
    'author': 'Alexandra Suarez',
    'license': 'LGPL-3',
    'category': 'Music School',
    'depends': [
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/music_school_student_views.xml',
        'views/music_school_instrument_views.xml',
        'views/music_school_menuitems.xml',
    ],
    'installable': True,
    'application': True,
}
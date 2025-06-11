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
       'data/ir_cron.xml',
        'data/music_school_data.xml',
        'security/res_groups.xml',          # Grupos de acceso
        'security/ir.model.access.csv',         # Reglas de acceso
        'views/music_school_student_views.xml',
        'views/music_school_instrument_views.xml',
        'views/music_school_teacher_views.xml',
        'views/music_school_course_views.xml',
        'views/music_school_room_views.xml',
        'views/music_school_lesson_views.xml',
        'views/music_school_lesson_attendance_views.xml',
        'views/music_school_exam_views.xml',
        'views/music_school_menuitems.xml',
        'wizard/music_school_course_change_state_wizard.xml',
        'wizard/music_school_create_lesson_wizard.xml'
    ],
    'installable': True,
    'application': True,
}
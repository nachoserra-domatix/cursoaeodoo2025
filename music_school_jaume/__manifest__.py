{
    'name': 'Music School',
    'version': '18.0.0.0.0',
    'description': 'Manages a music school with students, teachers, and classes.',
    'summary': 'Manages a music school with students, teachers, and classes.',
    'author': 'Jaume Tor',
    'license': 'LGPL-3',
    'category': 'Music School',
    'depends': [
        'base',
    ],
    'data':[
        'data/ir_cron.xml',
        'data/music_school_data.xml',
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/music_school_student_views.xml',
        'views/music_school_instrument_views.xml',
        'views/music_school_teacher_views.xml',
        'views/music_school_course_views.xml',
        'views/music_school_room_views.xml',
        'views/music_school_lesson_views.xml',
        'views/music_school_lesson_attendance_views.xml',
        'views/music_school_exam_views.xml',
        'views/music_school_menuitems.xml',
        'wizard/music_school_course_change_state.xml',
        'wizard/music_school_lesson_batch.xml',
        'report/music_school_course_report.xml'
    ]
}
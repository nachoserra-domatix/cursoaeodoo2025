from odoo import models, fields

"""
    Este modelo gestiona las lecciones impartidas en la escuela de música.
    Cada lección está asociada a un curso específico y a un profesor responsable. Los campos incluyen:
    - teacher_id: El profesor encargado de la lección.
    - course_id: El curso al que está asociada la lección.
    - room_id: La sala donde se lleva a cabo la lección.
    - date: La fecha y hora en que se realiza la lección.
    - duration: La duración de la lección en horas.
    - notes: Notas adicionales sobre la lección.
    - color: Color asociado a la lección para las vistas de calendario.
    - state: Estado actual de la lección (borrador, finalizada, pospuesta, cancelada).
    - attendance_ids: Registros de asistencia relacionados con la lección.
"""

class MusicSchoolLesson(models.Model):
    _name = 'music.school.lesson'
    _description = 'Lessons'
    _rec_name = 'course_id'


    teacher_id = fields.Many2one(
        comodel_name='music.school.teacher',
        string="Teacher",
        help="Teacher responsible for the lesson"
    )
    course_id = fields.Many2one(
        comodel_name='music.school.course',
        string="Course",
        help="Course associated with the lesson"
    )
    room_id = fields.Many2one(
        comodel_name='music.school.room',
        string="Room",
        help="Room where the lesson takes place"
    )
    date = fields.Datetime(
        string="Date",
        help="Date and time when the lesson takes place",
        default=fields.Datetime.now
    )
    duration = fields.Float(
        string="Duration (hours)",
        help="Duration of the lesson in hours"
    )
    notes = fields.Text(
        string="Notes",
        help="Additional notes about the lesson"
    )

    color = fields.Integer(
        string="Color",
        help="Color associated with the lesson for calendar views"
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('done', 'Done'),
            ('postponed', 'Postponed'),
            ('cancelled', 'Cancelled'),
        ],
        string="State",
        default='draft',
        help="Current state of the lesson",
        group_expand='group_expand_state'
    )

    attendance_ids = fields.One2many(
        comodel_name='music.school.lesson.attendance',
        inverse_name='lesson_id',
        string="Attendance Records",
        help="Attendance records for the lesson"
    )

    def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]
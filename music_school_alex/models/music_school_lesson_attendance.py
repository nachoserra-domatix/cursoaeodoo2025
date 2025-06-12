from odoo import models, fields

"""
    Este modelo epresenta la asistencia a las lecciones en la escuela de música.
    Se tiliza para registrar la asistencia de los estudiantes a las lecciones de música.
    Cada registro de asistencia está vinculado a una lección específica y a un estudiante. 
    Los campos incluyen:
    - lesson_id: La lección a la que se registra la asistencia.
    - student_id: El estudiante cuya asistencia se está registrando.
    - is_present: Indica si el estudiante estuvo presente.
    - date: La fecha y hora del registro de asistencia.
    - notes: Notas adicionales sobre el registro de asistencia.
 
"""

class MusicSchoolLessonAttendance(models.Model):
    _name = 'music.school.lesson.attendance'
    _description = 'Attendance for Music School Lessons'
    _rec_name = 'student_id'

    lesson_id = fields.Many2one(
        comodel_name='music.school.lesson',
        string="Lesson",
        help="Lesson for which the attendance is recorded",
    )

    student_id = fields.Many2one(
        comodel_name='music.school.student',
        string="Student",
    )
    is_present = fields.Boolean(
        string="Is Present",
    )

    date = fields.Datetime(
        string="Date",
        help="Date and time of the attendance record",)
    
    notes = fields.Text(
        string="Notes",
        help="Additional notes about the attendance record",
    )
    
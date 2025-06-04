from odoo import models, fields

class MusicSchoolLessonAttendance(models.Model):
    _name = "music.school.lesson.attendance"
    _description = "Attendance for Music School Lesson "
    _rec_name = "student_id"

    lesson_id = fields.Many2one(
        comodel_name="music.school.lesson",
        string="Lesson",
        help="Lesson for which attendance is recorded"
    )
    
    student_id = fields.Many2one(
        comodel_name="music.school.student",
        string="Student",
    )
    present = fields.Boolean(
        string="Present",
        help="Indicates if the student was present in the lesson"
    )
    date = fields.Date(
        string="Date",
        help="Date of the lesson"
    )
    notes = fields.Text(
        string="Notes",
        help="Additional notes about the attendance"
    )
    
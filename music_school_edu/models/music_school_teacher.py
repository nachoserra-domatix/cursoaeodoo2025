from odoo import models, fields

class MusicSchoolTeacher(models.Model):
    _name = "music.school.teacher"
    _description = "Music School Teacher"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(String="Email")
    phone = fields.Char(String="Phone")
    reference = fields.Char(String="Reference")
    course_id = fields.One2many(
        comodel_name="music.school.course",
        inverse_name="teacher_id",
        string="Courses",
        help="Courses taught by the teacher"
    )

    lesson_id = fields.One2many(
        comodel_name="music.school.lesson",
        inverse_name="teacher_id",
        string="Lessons",
        help="Lessons conducted by the teacher"
    )
    level = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced')
        ],
        string="Level",
        default='beginner',
    )
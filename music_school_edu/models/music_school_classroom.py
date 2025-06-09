from odoo import models, fields

class MusicSchoolClassroom(models.Model):
    _name = "music.school.classroom"
    _description = "Music School Classroom"

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(string="Capacity", help="Maximum number of students allowed in the classroom")
    location = fields.Char(string="Location", help="Physical location of the classroom")
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course",
        help="Course associated with this classroom"
    )
    lesson_id = fields.One2many(
        comodel_name="music.school.lesson",
        inverse_name="classroom_id",
        string="Lessons",
        help="Lessons scheduled in this classroom"
    )
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The classroom name must be unique.'),
        ('capacity_positive', 'CHECK(capacity > 0)', 'The capacity must be a positive number.')
    ]
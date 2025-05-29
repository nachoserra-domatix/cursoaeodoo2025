from odoo import models, fields

class MusicSchoolLesson(models.Model):
    _name = "music.school.lesson"
    _description = "Music School Lesson"

    name = fields.Char(string="Name", required=True)
    notes = fields.Html(string="Description", help="Details about the lesson")
    date = fields.Datetime(string="Date", help="Date when the lesson is scheduled")
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course",
        help="Course associated with this lesson"
    )
    teacher_id = fields.Many2one(
        comodel_name="music.school.teacher",
        string="Teacher",
        help="Teacher conducting the lesson"
    )
    classroom_id = fields.Many2one(
        comodel_name="music.school.classroom",
        string="Classroom",
        help="Classroom where the lesson takes place"
    )
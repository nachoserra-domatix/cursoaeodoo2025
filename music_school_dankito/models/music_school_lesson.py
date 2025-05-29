from odoo import models, fields


class MusicSchoolLesson(models.Model):

    _name = "music.school.lesson"
    _description = "Music School Lessons"

    teacher_id = fields.Many2one(
        comodel_name="music.school.teacher",
        string="Teacher"
    )
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course"
    )
    classroom_id = fields.Many2one(
        comodel_name="music.school.classroom",
        string="Classroom"
    )
    datetime_init = fields.Datetime(string="Init DateTime")
    duration = fields.Integer(string="Duration in hours")
    notes = fields.Text(string="Notes")

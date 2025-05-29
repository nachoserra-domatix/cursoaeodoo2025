from odoo import models, fields


class MusicSchoolLesson(models.Model):
    _name = 'music.school.lesson'
    _description = 'Lessons'

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
        help="Date and time when the lesson takes place"
    )
    duration = fields.Float(
        string="Duration (hours)",
        help="Duration of the lesson in hours"
    )
    notes = fields.Text(
        string="Notes",
        help="Additional notes about the lesson"
    )
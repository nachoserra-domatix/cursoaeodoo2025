from odoo import models, fields

class Lesson(models.Model):
    _name = 'music.school.lesson'
    _description = 'Lesson'

    professor_id = fields.Many2one('music.school.professor', string='Professor')
    course_id = fields.Many2one('music.school.course', string='Course')
    classroom_id = fields.Many2one('music.school.classroom', string='Classroom')
    start_datetime = fields.Datetime(string='Start Date and Time')
    duration = fields.Float(string='Duration (hours)')
    notes = fields.Text(string='Notes')

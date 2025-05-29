from odoo import models, fields


class MusicSchoolCourse(models.Model):

    _name = "music.school.course"
    _description = "Music School Course"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    state = fields.Selection([
        ("draft", "Draft"),
        ("progress", "In progress"),
        ("finished", "Finished")],
        string="Course current status", default="draft")

    teacher_id = fields.Many2one(comodel_name='music.school.teacher', string='Teacher')
    instrument_id = fields.Many2one(comodel_name='music.school.instrument', string='Instrument')
    level = fields.Selection([
        ('0', 'None'),
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High'),
    ], string='Level', default='1')

    date_ini = fields.Date(string="Init date")
    date_end = fields.Date(string="End date")

    capacity = fields.Integer(string="Capacity")

    def change_course_state_draft(self):
        self.change_course_state('draft')

    def change_course_state_progress(self):
        self.change_course_state('progress')

    def change_course_state_finished(self):
        self.change_course_state('finished')
    def change_course_state(self, state):
        if state in ('draft', 'progress', 'finished'):
            self.state = state

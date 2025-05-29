from odoo import models, fields

class Course(models.Model):
    _name = 'music.school.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Finished')
    ], string='Status', default='draft')
    professor_id = fields.Many2one('music.school.professor', string='Professor')
    instrument_id = fields.Many2one('music.school.instrument', string='Instrument')
    level = fields.Char(string='Level')
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    capacity = fields.Integer(string='Capacity')

    def action_set_draft(self):
        self.state = 'draft'

    def action_set_in_progress(self):
        self.state = 'in_progress'

    def action_set_done(self):
        self.state = 'done'
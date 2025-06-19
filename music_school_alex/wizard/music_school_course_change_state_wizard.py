from odoo import models, fields, api

class MusicSchoolCourseChangeState(models.TransientModel):
    _name = 'music.school.course.change.state.wizard'
    _description = 'Wizard to change the state of a music school course'

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('progress', 'In progress'),
            ('finished', 'Finished'),
        ],
        string="State",
    )

    def action_change_state(self):
        active_ids = self.env.context.get('active_ids', [])
        if active_ids:
            courses = self.env['music.school.course'].browse(active_ids)
            courses.write({'state': self.state})

    
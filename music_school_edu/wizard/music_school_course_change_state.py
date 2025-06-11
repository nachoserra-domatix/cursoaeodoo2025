from odoo import models, fields, api

class MusicSchoolCourseChangeState(models.TransientModel):
    _name = "music.school.course.change.state"
    _description = "Change State of Music School Course"

    state = fields.Selection(
        selection =[
            ('draft','Draft'),
            ('in progress','In Progress'),
            ('completed','Completed')
        ],
        string="State"
    )
    def action_change_state(self):
        active_ids = self.env.context.get('active_ids', [])
        if active_ids:
            courses = self.env['music.school.course'].browse(active_ids)
            courses.write({'state': self.state})
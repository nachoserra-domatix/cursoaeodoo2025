from odoo import models, fields, api
from datetime import timedelta

class MusicSchoolLessonBatch(models.TransientModel):
    _name = 'music.school.lesson.batch'
    _description = 'Wizard to create a batch of music school lessons'

    course_id = fields.Many2one(
        comodel_name='music.school.course',
        string="Course",
        required=True,
        help="Course for which the lessons are created"
    )
    start_date = fields.Datetime(
        string="Start Date",
        required=True,
        help="Start date for the lessons"
    )
    end_date = fields.Datetime(
        string="End Date",
        required=True,
        help="End date for the lessons"
    )

    def action_create_lessons(self):
        #import pdb;pdb.set_trace()
        lesson_obj = self.env['music.school.lesson']
        current_date = self.start_date
        lesson = self.env['music.school.lesson']
        while current_date <= self.end_date:
            #acumulem en la variable lesson les lessons creades
            lesson |= lesson_obj.create({
                'course_id': self.course_id.id,
                'start_datetime': current_date,
            })
            current_date += timedelta(days=1)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lessons',
            'res_model': 'music.school.lesson',
            'view_mode': 'list,form',
            'domain': [('id', 'in', lesson.ids)],
            'target': 'current',
        }
from datetime import timedelta
from odoo import models, fields, api

class MusicSchoolLessonCreateWizard(models.TransientModel):
    _name = "music.school.lesson.create.wizard"
    _description = "Create Music School Lesson Wizard"

    
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course",
        required=True,
        help="Course to which the lesson belongs"
    )
    
    start_date = fields.Datetime(
        string="Start Date",
        required=True,
        help="Start date and time of the lesson"
    )
    end_date = fields.Datetime(
        string="End Date",
        required=True,
        help="End date and time of the lesson"
    )

    def action_create_lesson(self):
        lesson_obj = self.env['music.school.lesson']
        current_date = self.start_date
        lesson = self.env['music.school.lesson']
        while current_date <= self.end_date:
            lesson |= lesson_obj.create({
                'course_id': self.course_id.id,
                'date': current_date,
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
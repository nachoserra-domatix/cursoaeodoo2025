from odoo import models, fields


class MusicSchoolTeacher(models.Model):
    _name = 'music.school.teacher'
    _description = 'Teachers'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    level = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        string="Level",
        default='beginner',
    )

    course_count = fields.Integer(
        string="Courses Count",
        compute='_compute_course_count',
        help="Number of courses taught by this teacher"
    )

    def _compute_course_count(self):
        for record in self:
            record.course_count = self.env['music.school.course'].search_count([('teacher_id', '=', record.id)])

    def action_view_courses(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Courses',
            'res_model': 'music.school.course',
            'view_mode': 'list,form',
            'domain': [('teacher_id', '=', self.id)],
            'context': {'default_teacher_id': self.id},
        }
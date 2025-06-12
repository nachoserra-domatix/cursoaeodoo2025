from odoo import models, fields, api


class MusicSchoolStudent(models.Model):
    _name = 'music.school.student'
    _description = 'Students'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Partner",
        help="Partner associated with this student",
        copy=False
    )
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone", related="partner_id.phone", store=True, readonly=False)
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        help="Responsible user for this student",
        copy=False,
        default=lambda self: self.env.user
    )
    notes = fields.Html(
        string="Notes",
        help="Additional notes about the student",
        copy=False
    )

    reference = fields.Char(
        string="Reference",
        copy=False
    )

    attendances_count = fields.Integer(
        string="Attendances Count",
        compute='_compute_attendances_count',
        help="Number of attendance records for this student"
    )
    
    @api.onchange('partner_id')
    def _onchange_email(self):
        if self.partner_id:
            self.email = self.partner_id.email
        else:
            self.email = ''

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                age = today.year - record.birthdate.year
                record.age = age
            else:
                record.age = 0

    def generate_reference(self):
        for record in self:
            record.reference = f"ESC-{record.id}{record.name}"
    

    def action_view_attendances(self):
        self.ensure_one()
        action = self.env.ref("music_school_nacho.music_school_lesson_attendance_action").read()[0]
        action['domain'] = [('student_id', '=', self.id)]
        action['context'] = {'default_student_id': self.id}
        return action

    def _compute_attendances_count(self):
        for record in self:
            record.attendances_count = self.env['music.school.lesson.attendance'].search_count([('student_id', '=', record.id)])

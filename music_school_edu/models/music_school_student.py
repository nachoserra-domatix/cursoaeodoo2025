from odoo import models , fields, api

class MusicSchoolStudent(models.Model):
    _name = "music.school.student"
    _description = "music school student"
    _inherits = {'res.partner': 'partner_id'}

    # name = fields.Char(string="Name" ,required=True)
    # email = fields.Char(string="Email")
    # phone = fields.Char(string="Phone number",related ="partner_id.phone", store=True, readonly=False)
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    active = fields.Boolean(string="Active", default=True)
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        help="Partner associated with this student",
        copy=False,
        ondelete='cascade',
    )
    notes = fields.Html(
        string="Notes",
        help="Additional information about the student"
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        help="Responsible for this student",
        copy=False,
        default=lambda self: self.env.user
    )
    reference= fields.Char(string="Reference" ,copy = False)
    course_ids = fields.Many2many(
        comodel_name="music.school.course",
        string="Courses",
        help="Courses that the student is enrolled in"
    )
    attendance_ids = fields.One2many(
        comodel_name="music.school.lesson.attendance",
        inverse_name="student_id",
        string="Attendances",
        help="Attendance records for the student"
    )
    attendance_count = fields.Integer(
        string="Attendance Count",
        compute="_compute_attendance_count",
        help="Number of attendance records for the student"
    )
    def _compute_attendance_count(self):
        for record in self:
            record.attendance_count = self.env['music.school.lesson.attendance'].search_count([('student_id', '=', record.id)])
    def action_view_attendance(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attendances',
            'res_model': 'music.school.lesson.attendance',
            'view_mode': 'list,form',
            'domain': [('student_id', '=', self.id)],
            'context': {'default_student_id': self.id,'default_date': fields.Date.today()},
        }
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.email = self.partner_id.email
            self.phone = self.partner_id.phone

    def generate_reference(self):
        for record in self:
            record.reference = f"ESC-{record.id}{record.name[0:3].upper()}"
    
    @api.depends('birthdate')
    def _compute_age(self):
        from datetime import date
        for record in self:
            if record.birthdate:
                today = date.today()
                age = today.year - record.birthdate.year - ((today.month, today.day) < (record.birthdate.month, record.birthdate.day))
                record.age = age
            else:
                record.age = 0

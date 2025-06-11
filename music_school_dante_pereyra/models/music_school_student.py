from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class MusicSchoolStudent(models.Model):
    _name="music.school.student"
    _description="Students"

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age",compute="_compute_age")
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        help="Responsible user for this student"
    )
    notes = fields.Html(
        string="Notes",
        help="Additional notes about the student"
    )

    code = fields.Char(string="Code", readonly=True)

    def action_generar_matricula(self):
        for record in self:
            record.code = f"MAT-{record.id:05d}"

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = relativedelta(fields.Date.today(), record.birthdate).years
            else:
                record.age = 0

from odoo import models, fields, api
from datetime import  date

class MusicSchoolStudent(models.Model):

    _name = "music.school.student"
    _description = "School Music Student"

    active = fields.Boolean(string="Active", default=True)
    email = fields.Char(string="Email")
    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone number")
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="_compute_age")

    user_id = fields.Many2one(
        string="Responsible",
        help="Responsible User",
        comodel_name="res.users"
    )

    reference = fields.Char(string="Reference")

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                record.age = today.year - record.birthday.year - (
                        (today.month, today.day) < (record.birthday.month, record.birthday.day)
                )
            else:
                record.age = 0

    def generate_code(self):
        year = date.today().year
        name_txt = (self.name or '').strip().replace(' ', '').upper()
        self.reference = f"MAT/{year}/{name_txt}"


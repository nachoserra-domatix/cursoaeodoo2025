from odoo import models, fields
from datetime import  date

class MusicSchoolStudent(models.Model):

    _name = "music.school.student"
    _description = "School Music Student"

    active = fields.Boolean(string="Active", default=True)
    email = fields.Char(string="Email")
    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone number")
    birthday = fields.Date(string="Birthday")

    user_id = fields.Many2one(
        string="Responsible",
        help="Responsible User",
        comodel_name="res.users"
    )

    reference = fields.Char(string="Reference")

    def generate_code(self):
        year = date.today().year
        name_txt = (self.name or '').strip().replace(' ', '').upper()
        self.reference = f"MAT/{year}/{name_txt}"


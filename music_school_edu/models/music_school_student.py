from odoo import models , fields

class MusicSchoolStudent(models.Model):
    _name = "music.school.student"
    _description = "music school student"

    name = fields.Char(string="Name" ,required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone number")
    birthdate = fields.Date(string="Birth date")
    age = fields.Integer(string="Age")
    active = fields.Boolean(string="Active", default=True)
    notes = fields.Html(
        string="Notes",
        help="Additional information about the student"
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        help="Responsible for this student"
    )
    reference= fields.Char(string="Reference")

    def generate_reference(self):
        for record in self:
            record.reference = f"ESC-{record.id}{record.name[0:3].upper()}"

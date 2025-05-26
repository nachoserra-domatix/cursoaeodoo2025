from odoo import models, fields

class MusicSchoolStudent(models.Model):

    _name = "music.school.student"
    _description = "School Music Student"

    active = fields.Boolean(string="Active", default=True)
    email = fields.Char(string="Email")
    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone number")


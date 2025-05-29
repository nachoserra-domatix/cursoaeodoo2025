from odoo import models, fields


class MusicSchoolTeacher(models.Model):

    _name = "music.school.teacher"
    _description = "School Music Teacher"

    name = fields.Char(string="Name")
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")

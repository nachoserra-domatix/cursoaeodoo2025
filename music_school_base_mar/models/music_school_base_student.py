from odoo import models, fields

class MusicSchoolBaseStudent(models.Model):
    _name = 'music.school.base.student'
    _description = 'Music School Base Student'

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    phone = fields.Char(string="Phone")
    birthdate = fields.Date(string="Birthdate")
    studentimage = fields.Image(string="Avatar", max_width=300, max_height=300)   
    notes = fields.Text(string="Notes")
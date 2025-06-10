from odoo import models, fields


class MusicSchoolStudent(models.Model):
    _name = 'music.school.student'
    _description = 'Students'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age")
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        help="Responsible user for this student"
    )
    notes = fields.Html(
        string="Notes",
        help="Additional notes about the student"
    )
    

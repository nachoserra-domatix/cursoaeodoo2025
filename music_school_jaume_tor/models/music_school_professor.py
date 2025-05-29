from odoo import models, fields

class Professor(models.Model):
    _name = 'music.school.professor'
    _description = 'Professor'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

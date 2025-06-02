from odoo import models, fields

class MusicSchoolProfessor(models.Model):
   _name = "music.school.professor"
   _description = "Professors"

   name = fields.Char(string="Name", required=True)
   email = fields.Char(string="Email")
   phone = fields.Integer(string="Phone")
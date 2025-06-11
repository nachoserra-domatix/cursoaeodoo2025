from odoo import models, fields

class MusicSchoolClassroom(models.Model):
   _name = "music.school.classroom"
   _description = "Classrooms"

   name = fields.Char(string="Name", required=True)
   capacity = fields.Integer(string="Capacity")
   location = fields.Char(string="Location")

   _sql_constraints = [
      ('name_unique', 'UNIQUE(name)', 'The classroom name must be unique.'),
   ]
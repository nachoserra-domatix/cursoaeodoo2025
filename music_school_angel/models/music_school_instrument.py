from odoo import models, fields

class MusicSchoolInstrument(models.Model):
   _name = "music.school.instrument"
   _description = "Instruments"

   name = fields.Char(string="Name", required=True)
   description = fields.Text(string="Description")
   family = fields.Selection([('string', 'String'), ('wind', 'Wind'), ('percussion', 'Percussion')], string="Family", default='wind')
   last_maintenance = fields.Date(string="Last Maintenance")

   def instrument_maintenance(self):
      for record in self:
         record.last_maintenance = fields.Date.today(); 
   
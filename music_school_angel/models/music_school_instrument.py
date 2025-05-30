from odoo import models, fields

class MusicSchoolInstrument(models.Model):
   _name = "music.school.instrument"
   _description = "Instruments"

   name = fields.Char(string="Name", required=True)
   description = fields.Text(string="Description")
   family = fields.Selection([('Cuerda', 'Cuerda'), ('Viento', 'Viento'), ('Percusion', 'Percusión')], string="Family", default='Viento')
   last_maintenance = fields.Date(string="Last Maintenance")

   def instrument_maintenance(self):
      for record in self:
         record.last_maintenance = fields.Date.today(); 
   
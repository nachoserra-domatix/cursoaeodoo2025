from odoo import models, fields

class MusicSchoolInstrument(models.Model):

    _name = "music.school.instrument"
    _description = "Music School Instrument"

    name = fields.Char(string="Instrument name")
    description = fields.Text(string="Description")
    family = fields.Selection(
        selection=[
            ('string', 'String'),
            ('wind', 'Wind'),
            ('percussion', 'Percussion'),
        ],
        string='Family',
        required=True
    )

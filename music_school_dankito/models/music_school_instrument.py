from odoo import models, fields
from datetime import date

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

    last_revision_date = fields.Date(string="Last revision date")

    def set_last_revision_date(self):
        today = date.today()
        self.last_revision_date = today

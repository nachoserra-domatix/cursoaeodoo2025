from odoo import models, fields


class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Instruments'

    name = fields.Char(string="Name", required=True, translate=True)
    family = fields.Selection(
        selection=[
            ('string', 'String'),
            ('wind', 'Wind'),
            ('percussion', 'Percussion'),
            ('keyboard', 'Keyboard'),
            ('electronic', 'Electronic'),
        ],
        string="Family",
        required=True,
    )
    description = fields.Text(string="Description")
    last_maintenance_date = fields.Date(
        string="Last Maintenance Date",
        help="Date of the last maintenance performed on the instrument"
    )

    def instrument_maintenance(self):
        for record in self:
            record.last_maintenance_date = fields.Date.today()
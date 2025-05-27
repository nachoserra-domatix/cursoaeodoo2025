from odoo import models, fields

class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Music School Instrument'

    name = fields.Char(string='Name', required=True)
    family = fields.Selection(
        selection=[
            ('string', 'String'),
            ('wind', 'Wind'),
            ('percussion', 'Percussion'),
            ('keyboard', 'Keyboard'),
        ],
        string='Family',
        required=True
    )
    state = fields.Selection(
        selection=[
            ('available', 'Available'),
            ('rented', 'Rented'),
            ('maintenance', 'Maintenance'),
        ],
        string='State',
        default='available'
    )
    manufacturer = fields.Char(string='Manufacturer')
    description = fields.Html(
        string="Description",
        help="Additional information about the Instrument"
    )
    
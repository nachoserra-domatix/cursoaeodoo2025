from odoo import models, fields
class MusicSchoolInstrumentFamily(models.Model):
    _name = 'music.school.instrument.family'
    _description = 'Instrument Family'

    name = fields.Char(string='Name', required=True, translate=True)
    
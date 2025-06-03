from odoo import models, fields

class MusicSchoolBaseInstrument(models.Model):
    _name = 'music.school.base.instrument'
    _description = 'Music School Base instrument'

    name = fields.Char(string="Name", required=True)
    family = fields.Selection([
        ('string', 'Cuerda'),
        ('wind', 'Viento'),
        ('percussion', 'Percusión'),
        ('keyboard', 'Teclado'),
    ], string="Family", required=True)

    instrumentimage = fields.Image(string="Instrument image", max_width=300, max_height=300)   
    description  = fields.Text(string="Description")
    active = fields.Boolean(string="Activo", default=True)
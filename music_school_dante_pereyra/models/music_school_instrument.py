from odoo import models, fields

class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Instrumento de Escuela de Música'

    name = fields.Char(string='Nombre', required=True)
    family = fields.Selection([
        ('cuerda', 'Cuerda'),
        ('viento', 'Viento'),
        ('percusion', 'Percusión')
    ], string='Familia', required=True)
    description = fields.Text(string='Descripción')
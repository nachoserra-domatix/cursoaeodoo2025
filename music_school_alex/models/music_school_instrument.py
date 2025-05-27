from odoo import models, fields

'''
    Este modelo representa los instrumentos de la escuela de musica 
    incluye los campos para el nombre, la familia y descripcion.

    Tambien utilizamos el campo seleccion, para seleccionar el tipo de 
    intrumento de familia. 
'''

class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Instruments'

    name = fields.Char(string="Name", required=True)
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
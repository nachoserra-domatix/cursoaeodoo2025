from odoo import models, fields

"""
    En este modelo representamos las familias de instrumentos de la escuela.
    -Se almacena la información relacionada con las diferentes familias de instrumentos,
    permitiendo categorizar y organizar los instrumentos disponibles en la institución. 
    -Cada familia de instrumentos puede incluir varios tipos de instrumentos, facilitando así la gestión y 
    clasificación de los mismos. El campo 'name' es obligatorio y se traduce para soportar múltiples 
    idiomas en la interfaz de usuario.
"""
class MusicSchoolInstrumentFamily(models.Model):
    _name = 'music.school.instrument.family'
    _description = 'Instruments'

    name = fields.Char(string="Name", required=True, translate=True)
    
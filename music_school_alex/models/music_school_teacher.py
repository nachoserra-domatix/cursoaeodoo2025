from odoo import models, fields

'''
    Este modelo almacena información sobre los profesores, sus datos personales
    y nivel de enseñanza. Los campos incluyen:
    - name: Nombre del profesor (requerido).
    - email: Correo electrónico del profesor.
    - phone: Teléfono del profesor.
    - level: Nivel de enseñanza del profesor, con opciones para 'Beginner', 'Intermediate', y 'Advanced'.
      El nivel predeterminado es 'Beginner'.
'''

class MusicSchoolTeacher(models.Model):
    _name = 'music.school.teacher'
    _description = 'Teachers'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    level = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        string="Level",
        default='beginner',
    )
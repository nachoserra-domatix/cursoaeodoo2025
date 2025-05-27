from odoo import models, fields

''' Este modelo representa a los estudiantes de la escuela de 
    musica, tenemos informacion de sus datos personales con
    campos de tipo char, int y fecha

    Tambien se maneja un estado booleano activo
    por defecto = true 
'''
class MusicSchoolStudent(models.Model):
    _name = 'music.school.student' 
    _description = 'Students'      

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age")
    
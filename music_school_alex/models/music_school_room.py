from odoo import models, fields

"""
    Este modelo se utiliza para gestionar los salones disponibles en la escuela de música.
    Cada salon tiene un nombre, una capacidad máxima y una ubicación física dentro de la escuela.
    Los campos incluyen:
    - name: Nombre de la sala (requerido).
    - capacity: Capacidad máxima de estudiantes que puede albergar la sala.
    - location: Ubicación física de la sala dentro de la escuela.
    Tiene una restricción única en el nombre del salon para asegurar que no haya
    duplicados en la base de datos.
"""

class MusicSchoolRoom(models.Model):
    _name = 'music.school.room'
    _description = 'Rooms'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer(
        string="Capacity",
        help="Maximum number of students that can fit in the room"
    )
    location = fields.Char(
        string="Location",
        help="Physical location of the room within the school"
    )

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The room name must be unique.'),
    ]
from odoo import models, fields


class MusicSchoolClassroom(models.Model):

    _name = "music.school.classroom"
    _description = "Music School Classroom"

    name = fields.Char(string="Classroom name")
    location = fields.Char(string="Location")
    capacity = fields.Integer(string="Classroom max. students capacity")
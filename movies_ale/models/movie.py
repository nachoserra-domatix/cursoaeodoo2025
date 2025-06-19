from odoo import models, fields

class Movie(models.Model):
    _name = 'movies.ale.movie'
    _description = 'Movies'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Descrition")
    duration = fields.Integer(string="Duration (min)")
    genre = fields.Selection([
        ('thriller', 'Thriller'),
        ('comedy', 'Comedy'),
        ('action', 'Action'),
        ('horror', 'Horror'),
        ('documentary', 'Documentary') 
    ])
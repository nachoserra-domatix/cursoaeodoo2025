from odoo import models, fields

class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Music School Instrument'

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
    last_maintenance_date = fields.Date(string="Last revision")
    last_check_date = fields.Date(string="Last maintenance")

    def action_set_today_dates(self):
        today = fields.Date.today()
        for record in self:
            record.last_maintenance_date = today
            record.last_check_date = today
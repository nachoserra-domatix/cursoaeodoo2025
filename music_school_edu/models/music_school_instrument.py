from odoo import models, fields , api

class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Music School Instrument'

    name = fields.Char(string='Name', required=True)
    family_id = fields.Many2one(
        comodel_name='music.school.instrument.family',
        string="Family",
        help="Family of the instrument"
    )
    # family = fields.Selection(
    #     selection=[
    #         ('string', 'String'),
    #         ('wind', 'Wind'),
    #         ('percussion', 'Percussion'),
    #         ('keyboard', 'Keyboard'),
    #     ],
    #     string='Family',
    #     required=True
    # )
    state = fields.Selection(
        selection=[
            ('available', 'Available'),
            ('rented', 'Rented'),
            ('maintenance', 'Maintenance'),
        ],
        string='State',
        default='available'
    )
    manufacturer = fields.Char(string='Manufacturer')
    description = fields.Html(
        string="Description",
        help="Additional information about the Instrument"
    )
    maintenance_date = fields.Date(
        string='Last maintenance date',
        help="Date on which the instrument was last serviced"
    )
    course_id = fields.One2many(
        comodel_name='music.school.course',
        inverse_name='instrument_id',
        string='Courses',
        help='Courses associated with this instrument'
    )
    repair = fields.Boolean(
        string='Repair',
        help='Indicates if the instrument is under repair',
        compute='repair_instrument',
        inverse='set_is_repaired',
    )
    def update_maintenance_date(self):
        for record in self:
            record.maintenance_date = fields.Date.today()
            
   
    def repair_instrument(self):
        for record in self:
            record.repair = bool(record.maintenance_date)

    def set_is_repaired(self):
        for record in self:
            if record.repair:
                record.maintenance_date = fields.Date.today()
            else:
                record.maintenance_date = False
            

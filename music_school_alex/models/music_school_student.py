from odoo import models, fields, api

''' Este modelo representa a los estudiantes de la escuela de 
    musica, tenemos informacion de sus datos personales con
    campos de tipo char, int y fecha

    Los campos incluyen:
    - active: Estado booleano que indica si el estudiante está activo (por defecto, True).
    - name: Nombre del estudiante (requerido).
    - partner_id: Relación con el modelo 'res.partner' para gestionar información adicional.
    - email: Correo electrónico del estudiante.
    - phone: Teléfono del estudiante, relacionado con el partner asociado.
    - birthdate: Fecha de nacimiento del estudiante.
    - age: Edad del estudiante, calculada a partir de la fecha de nacimiento.
    - user_id: Usuario responsable del estudiante, con un valor predeterminado del usuario actual.
    - notes: Notas adicionales sobre el estudiante.
    - reference: Referencia única para el estudiante.
'''

class MusicSchoolStudent(models.Model):
    _name = 'music.school.student'
    _description = 'Students'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Partner",
        help="Partner associated with this student"
    )
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone", related="partner_id.phone", store=True, readonly=False, copy=False)
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        help="Responsible user for this student",
        copy=False,
        default=lambda self: self.env.user
    )
    notes = fields.Html(
        string="Notes",
        help="Additional notes about the student",
        copy=False
    )

    reference = fields.Char(
        string="Reference",
        copy=False
    )
    
    @api.onchange('partner_id')
    def _onchange_email(self):
        if self.partner_id:
            self.email = self.partner_id.email
        else:
            self.email = ''

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                age = today.year - record.birthdate.year
                record.age = age
            else:
                record.age = 0

    def generate_reference(self):
        for record in self:
            record.reference = f"ESC-{record.id}{record.name}"










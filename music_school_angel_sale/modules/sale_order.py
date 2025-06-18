from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    course_id = fields.Many2one(
        comodel_name='music.school.course',
        string="Course",
        help="Course associated with the sale order"
    )

    # Sobreescriure mètode de la classe pare
    # def action_confirm(self):
    #     res = super().action_confirm()
    #     self.name = 'canvie el nom'
    #     self.description = 'canvie la descripció'
    #    return res
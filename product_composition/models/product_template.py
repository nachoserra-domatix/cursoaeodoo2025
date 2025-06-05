from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    composition_line_ids = fields.One2many(
        comodel_name='product.composition.line',
        inverse_name='product_tmpl_id',
        string='Compositions'
    )

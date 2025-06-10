from odoo import models, fields


class ProductCompositionLine(models.Model):
    _name = 'product.composition.line'
    _description = 'Product Composition Line'

    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product',
        required=True,
        ondelete='cascade'
    )
    percentage = fields.Float(string='Percentage')
    description_id = fields.Many2one(
        comodel_name='product.composition.description',
        string='Description',
        required=True,
        ondelete='restrict',
    )

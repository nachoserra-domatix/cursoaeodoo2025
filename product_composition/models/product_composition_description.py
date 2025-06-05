from odoo import models, fields


class ProductCompositionDescription(models.Model):
    _name = 'product.composition.description'
    _description = 'Product Composition Description'

    name = fields.Char(required=True)


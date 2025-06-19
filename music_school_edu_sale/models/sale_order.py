from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    course_id = fields.Many2one(
        comodel_name='music.school.course',
        string='Course',
        help='Course associated with this sale order',
    )

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_id.course_ok:
                    course = self.env['music.school.course'].create({
                        'name': line.product_id.name,
                        'product_id': line.product_id.id,
                        'price': line.price_subtotal,
                    })
                    order.course_id = course.id
                    break
            else:
                order.course_id = False
        return res
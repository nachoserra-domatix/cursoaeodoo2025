from odoo import models, fields, api

class MusicSchoolCourse(models.Model):
    _inherit = 'music.school.course'

    price = fields.Float(
        string='Price',
        help='Price of the course',
        default=0.0,
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        help='Product associated with the course for sale purposes',
        domain="[('sale_ok', '=', True)]",
    )
    order_ids= fields.One2many(
        comodel_name='sale.order',
        inverse_name='course_id',
        string='Sales Orders',
        help='Sales orders associated with this course',
    )
    order_count = fields.Integer(
        string='Order Count',
        compute='_compute_order_count',
        help='Number of sales orders associated with this course',
    )

    def _compute_order_count(self):
        for record in self:
            record.order_count = len(record.order_ids)
    
    @api.depends('product_id')
    def onchange_product_id(self):
        for record in self:
            if record.product_id:
                record.price = record.product_id.list_price
            else:
                record.price = 0.0
    def action_create_orders(self):
        self.order_ids.unlink()
        for student in self.student_ids:
            order = self.env['sale.order'].create({
                'partner_id': student.partner_id.id,
                'course_id': self.id,
                'date_order': fields.Datetime.now(),
                'company_id': self.env.company.id,
            })
            self.env['sale.order.line'].create({
                'order_id': order.id,
                'product_id': self.product_id.id,
                'price_unit': self.price,
                'product_uom_qty': 1.0,
            })
    def action_view_orders(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Sales Orders',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.order_ids.ids)],
        }
    
    def action_cancel(self):
        res = super().action_cancel()
        self.order_ids.action_cancel()
        return res
    
    def action_draft(self):
        res = super().update_state_draft()
        self.order_ids.action_draft()
        return res
    
    def action_finish(self):
        res = super().update_state_complete()
        self.order_ids.filtered(lambda o: o.state != 'done').action_confirm()
        self.order_ids.filtered(lambda o: o.state != 'invoiced')._create_invoices()
        return res
    
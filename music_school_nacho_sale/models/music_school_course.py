from odoo import models, fields, api


class MusicSchoolCourse(models.Model):
    _inherit = 'music.school.course'

    price = fields.Float(
        string="Price",
        help="Price of the course",
        default=0.0
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Product",
        help="Product associated with the course for sales purposes",
    )

    order_ids = fields.One2many(
        comodel_name='sale.order',
        inverse_name='course_id',
        string="Orders",
        help="Sales orders associated with the course"
    )

    order_count = fields.Integer(
        string="Orders Count",
        compute='_compute_order_count',
        help="Number of sales orders associated with the course"
    )

    def _compute_order_count(self):
        for record in self:
            record.order_count = len(record.order_ids)

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.price = self.product_id.list_price
        else:
            self.price = 0.0
    
    def action_create_orders(self):
        self.order_ids.unlink()
        for student in self.student_ids:
            order = self.env['sale.order'].create({
                'partner_id': student.partner_id.id,
                'course_id': self.id,
                'date_order': fields.Datetime.now(),
                'company_id': self.company_id.id,
            })
            self.env['sale.order.line'].create({
                'order_id': order.id,
                'product_id': self.product_id.id,
                'price_unit': self.price,
                'product_uom_qty': 1.0,
            })
    def action_view_orders(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Orders',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.order_ids.ids)],
        }
    
    def write(self, vals):
        if 'student_ids' in vals:
            for record in self:
                student_ids_commands = vals['student_ids']
                removed_student_ids = [cmd[1] for cmd in student_ids_commands if cmd[0] == 3]
                removed_students = self.env['music.school.student'].browse(removed_student_ids)
                if removed_student_ids:
                    # Unlink orders for removed students
                    orders_to_unlink = self.env['sale.order'].search([
                        ('course_id', '=', record.id),
                        ('partner_id', 'in', removed_students.partner_id.ids)
                    ])
                    orders_to_unlink.unlink()
        res = super().write(vals)
        return res

    def action_cancel(self):
        res = super().action_cancel()
        self.order_ids.action_cancel()
        return res

    def action_draft(self):
        res = super().action_draft()
        self.order_ids.action_draft()
        return res

    def action_finish(self):
        res = super().action_finish()
        self.order_ids.filtered(lambda o: o.state != 'done').action_confirm()
        self.order_ids.filtered(lambda o: o.invoice_status != 'invoiced')._create_invoices()
        return res
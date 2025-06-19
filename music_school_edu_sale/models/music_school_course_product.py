from odoo import models, fields, api

class MusicSchoolCourseProduct(models.Model):
    _inherit = 'product.template'

    course_ok = fields.Boolean(
        string='Is a Course',
        help='Indicates if this product is a course',
        default=False,
    )
    type = fields.Selection(
        selection_add=[('course', 'Course')],
        ondelete={'course': 'set default'},
    )

    def _create_course(self):
        for product in self:
            if product.course_ok:
                course = self.env['music.school.course'].create({
                    'name': product.name,
                    'product_id': product.id,
                    'price': product.list_price,
                })
                product.course_id = course.id
            else:
                product.course_id = False



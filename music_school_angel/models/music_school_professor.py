from odoo import models, fields

class MusicSchoolProfessor(models.Model):
   _name = "music.school.professor"
   _description = "Professors"
   _inherits = {'res.partner': 'partner_id'}

   #name = fields.Char(string="Name", required=True)
   #email = fields.Char(string="Email")
   #phone = fields.Integer(string="Phone")
   partner_id = fields.Many2one(
      comodel_name='res.partner',
      string="Partner",
      help="Partner associated with this professor",
      copy=False,
      ondelete='cascade',
   )

   level = fields.Selection(
      selection=[
         ('beginner', 'Beginner'),
         ('intermediate', 'Intermediate'),
         ('advanced', 'Advanced'),
         ],
         string="Level",
         default='beginner'
      )

   course_count = fields.Integer(
        string="Courses Count",
        compute='_compute_course_count',
        help="Number of courses taught by this professor"
   )

   def _compute_course_count(self):
      for record in self:
         record.course_count = self.env['music.school.course'].search_count([('professor_id', '=', record.id)])


   def action_view_courses(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Courses',
            'res_model': 'music.school.course',
            'view_mode': 'list,form',
            'domain': [('professor_id', '=', self.id)],
            'context': {'default_professor_id': self.id},
        }

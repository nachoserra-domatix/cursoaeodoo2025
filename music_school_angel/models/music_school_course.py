from odoo import models, fields

class MusicSchoolCourse(models.Model):
   _name = "music.school.course"
   _description = "Courses"

   name = fields.Char(string="Name", required=True)
   description = fields.Text(string="Description")
   state = fields.Selection([('draft', 'Draft'), ('progress', 'In progress'), ('finished', 'Finished')], string="State", default='draft', group_expand='group_expand_state')

   professor_id = fields.Many2one(
      comodel_name='music.school.professor',
      string="Professor",
      help="Professor of this course",
   )

   instrument_id = fields.Many2one(
      comodel_name='music.school.instrument',
      string="Instrument",
      help="Instrument of the course",
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

   start_date = fields.Date(string="Start Date")
   end_date = fields.Date(string="End Date")
   capacity = fields.Integer(string="Capacity")

   color = fields.Integer(
        string="Color",
        help="Color associated with the course for calendar views"
    )

#
   def action_draft(self):
      for record in self:
         record.state = "draft"

   def action_progress(self):
      for record in self:
         record.state = "progress"

   def action_finish(self):
      for record in self:
         record.state = "finished"

   def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]
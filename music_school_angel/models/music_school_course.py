from odoo import models, fields, api

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

   student_ids = fields.Many2many(
        comodel_name='music.school.student',
        string="Students",
        help="Students enrolled in the course"
    )

   day_duration = fields.Integer(
        string="Duration day",
        compute='_compute_day_duration',
        help="Duration of the course in days",
        store=True
   )

   @api.depends('start_date', 'end_date')
   def _compute_day_duration(self):
      for record in self:
         if record.start_date and record.end_date:
               start = fields.Date.from_string(record.start_date)
               end = fields.Date.from_string(record.end_date)
               record.day_duration = (end - start).days + 1
         else:
               record.day_duration = 0


   def action_draft(self):
      for record in self:
         record.state = "draft"

   def action_progress(self):
      for record in self:
         record.state = "progress"

   def action_finish(self):
      for record in self:
         record.state = "finished"
         lessons = self.env['music.school.lesson'].search([('course_id','=', record.id)])
         #lessons.state = 'done'
         lessons.write({'state': 'done'})

   def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]

   def create_lesson(self):
      vals = {
         'course_id': self.id,
         'professor_id': self.professor_id.id,
      }
      lesson = self.env['music.school.lesson'].create(vals)

   def assign_students(self):
        for record in self:
            students = self.env['music.school.student'].search([])
            if students:
                #record.student_ids = [(6, 0, students.ids)]
                #record.write({'student_ids': [(6, 0, students.ids)]})
                record.student_ids = students
                #record.student_ids = [Command.set(students.ids)]
                #record.write({
                #     'student_ids': [Command.set(student.ids)]
                # })
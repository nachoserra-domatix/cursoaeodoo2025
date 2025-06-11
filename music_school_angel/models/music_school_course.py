from odoo import models, fields, api
from odoo.exceptions import UserError

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

   start_date = fields.Date(
      string="Start Date",
      help="Date when the course starts",
      default=fields.Date.context_today,
   )
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

   exam_count = fields.Integer(
      string="Exams Count",
      compute='_compute_exam_count',
      help="Number of exams associated with the course"
   )

   lesson_count = fields.Integer(
      string="Lessons Count",
      compute='_compute_lesson_count',
      help="Number of lessons associated with the course"
   )

   #Restricció en base de dades. Camp nom únic
   _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The course name must be unique.'),
   ]

   def _compute_lesson_count(self):
      for record in self:
         record.lesson_count = self.env['music.school.lesson'].search_count([('course_id', '=', record.id)])
         
   def _compute_exam_count(self):
      for record in self:
         record.exam_count = self.env['music.school.exam'].search_count([('course_id', '=', record.id)])
         #record.exam_count = len(self.env['music.school.exam'].search([('course_id', '=', record.id)]))

   #La data fi no pot ser anterior a l'inici
   @api.constrains('start_date', 'end_date')
   def _check_dates(self):
      for record in self:
         if record.start_date and record.end_date:
               if record.start_date > record.end_date:
                  raise UserError("Start date cannot be after end date.")
         else:
               raise UserError("Both start date and end date must be set.")


   #S'executa cada vegada que es guarda el curs i s'ha modificat la capacitat
   @api.constrains('capacity')
   def _check_capacity(self):
      for record in self:
         if record.capacity < 0:
            raise UserError("Capacity cannot be negative.")


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

   def finish_courses(self):
        courses = self.env['music.school.course'].search([('state', '!=', 'finished'), ('end_date', '<=', fields.Date.context_today(self))])
        courses.action_finish()

   def action_view_exams(self):
      return {
         'type': 'ir.actions.act_window',
         'name': 'Exams',
         'res_model': 'music.school.exam',
         'view_mode': 'kanban,pivot,list,form',
         'domain': [('course_id', '=', self.id)],
         'context': {'default_course_id': self.id},
      }
    
   def action_view_lessons(self):
      return {
         'type': 'ir.actions.act_window',
         'name': 'Lessons',
         'res_model': 'music.school.lesson',
         'view_mode': 'list,form',
         'domain': [('course_id', '=', self.id)],
         'context': {'default_course_id': self.id},
      }
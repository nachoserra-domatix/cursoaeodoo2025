from odoo import models, fields

class MusicSchoolLesson(models.Model):
   _name = "music.school.lesson"
   _description = "Lessons"
   _rec_name = 'course_id'

   professor_id = fields.Many2one(
      comodel_name='music.school.professor',
      string="Professor",
      help="Professor who teaches this lesson"
   )

   course_id = fields.Many2one(
      comodel_name='music.school.course',
      string="Course",
      help="Course of this lesson"
   )

   classroom_id = fields.Many2one(
      comodel_name='music.school.classroom',
      string="Classroom",
      help="Classroom where the lesson is teached."
   )

   start_datetime = fields.Datetime(string="Start DateTime")
   duration = fields.Integer(string="Duration (minutes)")
   notes = fields.Text(string="Notes")

   color = fields.Integer(
        string="Color",
        help="Color associated with the lesson for calendar views"
   )

   state = fields.Selection(
      selection=[
         ('draft', 'Draft'),
         ('done', 'Done'),
         ('postponed', 'Postponed'),
         ('cancelled', 'Cancelled'),
      ],
      string="State",
      default='draft',
      help="Current state of the lesson",
      group_expand='group_expand_state'
    )

   def group_expand_state(self, states, domain):
      return [key for key, val in type(self).state.selection]
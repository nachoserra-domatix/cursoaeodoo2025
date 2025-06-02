from odoo import models, fields

class MusicSchoolLesson(models.Model):
   _name = "music.school.lesson"
   _description = "Lessons"

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
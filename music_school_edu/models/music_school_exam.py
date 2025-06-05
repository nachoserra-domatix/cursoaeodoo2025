from odoo import models, fields
class MusicSchoolExam(models.Model):
    _name="music.school.exam"
    _description="Music School Exam"
    
    name= fields.Char(string = "Exam Name",help="Name of the exam")
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course",
        help="Course for which the exam is conducted"
    )
    date = fields.Datetime(
        string="Exam Date",
        help="Date and time of the exam"
    )
    instrument_id = fields.Many2one(
        comodel_name="music.school.instrument",
        string="Instrument",
        help="Instrument for which the exam is conducted"
    )
    min_note = fields.Float(
        string="Minimum Note",
        help="Minimum note required to pass the exam"
    )
    max_note = fields.Float(
        string="Maximum Note",
        help="Maximum note that can be achieved in the exam"
    )
    teacher_id = fields.Many2one(
        comodel_name="music.school.teacher",
        string="Teacher",
        help="Teacher conducting the exam"
    )
    exam_state= fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('in progress', 'In Progress'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        string="Exam State",
        default='draft',
        help="Current state of the exam",
        group_expand='group_expand_state'
    )
    result_ids = fields.One2many(
        comodel_name="music.school.exam.result",
        inverse_name="exam_id",
        string="Exam Results",
        help="Results of the exam for each student"
    )
    color = fields.Integer(
        string="Color",
        help="Color for the exam record in the calendar view"
    )
    def group_expand_state(self, states, domain):
        return [key for key, val in type(self).exam_state.selection]
    def assign_students(self):
        students = self.course_id.student_ids
        self.result_ids = [(0, 0, {'student_id': student.id}) for student in students]
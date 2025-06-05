from odoo import models, fields, Command, api


class MusicSchoolExam(models.Model):
    _name = 'music.school.exam'
    _description = 'Exams'


    name = fields.Char(string="Name", required=True)
    course_id = fields.Many2one(
        comodel_name='music.school.course',
        string="Course",
        help="Course associated with the exam"
    )
    instrument_id = fields.Many2one(
        comodel_name='music.school.instrument',
        string="Instrument",
        help="Instrument associated with the exam"
    )
    date = fields.Datetime(
        string="Date",
        help="Date and time of the exam"
    )
    min_score = fields.Float(
        string="Minimum Score",
        help="Minimum score required to pass the exam"
    )
    max_score = fields.Float(
        string="Maximum Score",
        help="Maximum score for the exam"
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('scheduled', 'Scheduled'),
            ('finished', 'Finished'),
        ],
        string="State",
        default='draft',
        group_expand='group_expand_state'
    )
    teacher_id = fields.Many2one(
        comodel_name='music.school.teacher',
        string="Teacher",
        help="Teacher responsible for the exam"
    )
    result_ids = fields.One2many(
        comodel_name='music.school.exam.result',
        inverse_name='exam_id',
        string="Results",
        help="Results of the exam for each student"
    )

    color = fields.Integer(
        string="Color",
        help="Color for the exam record in the calendar view"
    )

    def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]

    def assign_students(self):
        students = self.course_id.student_ids
        self.result_ids = [
            Command.create({
                'student_id': student.id,
            }) for student in students
        ]
        # self.result_ids = [(0, 0, {
        #     'student_id': student.id,
        #     'score': 0.0,  # Default score
        #     'passed': False,  # Default passed status
        # }) for student in students]

        # for student in students:
        #     self.env['music.school.exam.result'].create({
        #         'exam_id': self.id,
        #         'student_id': student.id,
        #     })
       
from odoo import models, fields, Command, api

class MusicSchoolExamResult(models.Model):
    _name = 'music.school.exam.result'
    _description = 'Exam Results'

    exam_id = fields.Many2one(
        comodel_name='music.school.exam',
        string="Exam",
        help="Exam associated with the result"
    )
    student_id = fields.Many2one(
        comodel_name='music.school.student',
        string="Student",
        help="Student who took the exam"
    )
    score = fields.Float(
        string="Score",
        help="Score obtained by the student in the exam"
    )

    passed = fields.Boolean(
        string="Passed",
        help="Indicates if the student passed the exam",
        compute='_compute_passed',
        store=True
    )
    notes = fields.Text(
        string="Notes",
        help="Additional notes about the exam result"
    )
    
    student_ids = fields.Many2many(
        comodel_name='music.school.student',
        string="Students",
        help="Students associated with the exam result",
        related="exam_id.course_id.student_ids")

    @api.depends('score', 'exam_id.min_score')
    def _compute_passed(self):
        for record in self:
            if record.score >= record.exam_id.min_score:
                record.passed = True
            else:
                record.passed = False
    
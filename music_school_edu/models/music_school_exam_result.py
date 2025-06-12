from odoo import models, fields , api

class MusicSchoolExamResult(models.Model):
    _name = "music.school.exam.result"
    _description = "Music School Exam Result"

    exam_id = fields.Many2one(
        comodel_name="music.school.exam",
        string="Exam",
        required=True,
        help="Exam for which the result is recorded"
    )
    student_id = fields.Many2one(
        comodel_name="music.school.student",
        string="Student",
        required=True,
        help="Student who took the exam"
    )
    note = fields.Float(
        string="Note",
        help="Note received by the student in the exam"
    )
    passed = fields.Boolean(
        string="Passed",
        compute="_compute_passed",
        help="Indicates if the student passed the exam based on the note",
        store=True
    )
    comments = fields.Text(
        string="Comments",
        help="Additional comments about the exam result"
    )
    # eligible_student_ids = fields.Many2many(
    #     comodel_name="music.school.student",
    #     compute="_compute_eligible_students",
    #     store=False,
    #     string="Eligible Students",
    #     help="Students eligible for the exam based on the course"
    # )
    # @api.depends('exam_id.course_id')
    # def _compute_eligible_students(self):
    #     for record in self:
    #         if record.exam_id.course_id:
    #             record.eligible_student_ids = self.env['music.school.student'].search([
    #                 ('course_ids', 'in', record.exam_id.course_id.id)
    #             ])
    #         else:
    #             record.eligible_student_ids = self.env['music.school.student']
    elegible_student_ids = fields.Many2many(
        comodel_name="music.school.student",
        related="exam_id.course_id.student_ids",
    )
                
    @api.depends( 'note')
    def _compute_passed(self):
        for record in self:
            record.passed = bool(record.exam_id and record.note >= record.exam_id.min_note)
from odoo import models, fields, Command, api
import logging
_logger = logging.getLogger(__name__)

"""
    Este modelo representa los exámenes de la escuela de música.
    -Almacena la información relacionada con los exámenes, incluyendo el nombre del examen,
    el curso y el instrumento asociados, la fecha y hora del examen, así como las puntuaciones mínima
    y máxima. 
    -Gestiona el estado del examen (borrador, programado o finalizado) 
    -Establece relaciones con los estudiantes y profesores involucrados. Además, permite registrar los resultados 
    de cada estudiante para cada examen.
"""
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
    
    def finish_exams(self):
        _logger.info("Buscando examenes en estado borrador o programado")
        exams = self.env['music.school.exam'].search([('state', 'in', ['draft','scheduled'])])
        for exam in exams:
            if exam.date and exam.date < fields.Datetime.now():
                exam.state = 'finished'
                _logger.info(f"Examen {exam.name} marcado como finalizado")
        _logger.info("Examenes finalizados correctamente")
       
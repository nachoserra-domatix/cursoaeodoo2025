from odoo import models , fields

class MusicSchoolCourse(models.Model):
    _name = "music.school.course"
    _description = "Music school course"

    name = fields.Char(string="Name" ,required=True)
    description = fields.Text(string="Desciption course")
    state = fields.Selection(
        selection =[
            ('draft','Draft'),
            ('in progress','In Progress'),
            ('completed','Completed')
        ],
        string="State"
    )
    teacher_id = fields.Many2one(
        comodel_name="music.school.teacher",
        string="Teacher",
        help="Teacher assigned to the course"
    )
    instrument_id = fields.Many2one(
        comodel_name="music.school.instrument",
        string="Instrument",
        help="Instrument associated with the course"
    )
    classroom_id = fields.Many2one(
        comodel_name="music.school.classroom",
        string="Classroom",
        help="Classroom where the course is conducted"
    )
    lesson_ids = fields.One2many(
        comodel_name="music.school.lesson",
        inverse_name="course_id",
        string="Lessons",
        help="Lessons included in this course"
    )
    level = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced')
        ],
        string="Level"
    )
    start_date = fields.Date(
        string="Start Date",
        help="Date when the course starts"
    )
    end_date = fields.Date(
        string="End Date",
        help="Date when the course ends"
    )
    capacity = fields.Integer(
        string="Capacity",
        help="Maximum number of students allowed in the course"
    )

    def update_state_complete(self):
        for record in self:
            record.state = 'completed'
    def update_state_in_progress(self):
        for record in self:
            record.state = 'in progress'
    def update_state_draft(self):
        for record in self:
            record.state = 'draft'

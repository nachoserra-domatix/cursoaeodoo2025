from odoo import models , fields , api

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
        ,default='draft',
        group_expand='group_expand_state',
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
            ('none', 'None'),
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        string="Level",
        default='beginner',
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
    color = fields.Integer(
        string="Color",
        help="Color for the course in the calendar view"
    )
    student_ids = fields.Many2many(
        comodel_name="music.school.student",
        string="Students",
        help="Students enrolled in the course"
    )
    course_duration = fields.Integer(
        string="Course Duration (days)",
        help="Duration of the course in days",
        compute="_compute_course_duration",
        store=True
    )

    @api.depends('start_date', 'end_date')
    def _compute_course_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                duration = (record.end_date - record.start_date).days
                record.course_duration = duration + 1
            else:
                record.course_duration = 0


    def update_state_complete(self):
        lessons = self.env['music.school.lesson'].search([('course_id', '=', self.id)])
        for record in self:
            record.state = 'completed'
        for lesson in lessons:
            lesson.state = 'completed'
            
    def update_state_in_progress(self):
        for record in self:
            record.state = 'in progress'
    def update_state_draft(self):
        for record in self:
            record.state = 'draft'
    def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]
    def create_lesson(self):
        vals= {
            'name':self.name + " Lesson",
            'course_id': self.id,
            'teacher_id': self.teacher_id.id,        
        }
        lesson = self.env['music.school.lesson'].create(vals)

    def assign_student(self):
        for record in self:
            students = self.env['music.school.student'].search([])
            if students:
                record.student_ids = [(6, 0, students.ids)]
                # record.student_ids = students 
                # record.student_ids = [Command.set(students.ids)]
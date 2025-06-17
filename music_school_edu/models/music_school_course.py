from odoo import models , fields , api
from odoo.exceptions import UserError

class MusicSchoolCourse(models.Model):
    _name = "music.school.course"
    _description = "Music school course"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    active= fields.Boolean(
        string="Active",
        default=True,
        help="Indicates if the course is currently active"
    )
    name = fields.Char(string="Name" ,copy=False)
    description = fields.Text(string="Desciption course",company_dependent=True, help="Description of the course")
    state = fields.Selection(
        selection =[
            ('draft','Draft'),
            ('in progress','In Progress'),
            ('completed','Completed'),
            ['cancelled','Cancelled'],
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
    lesson_count = fields.Integer(
        string="Lesson Count",
        compute="_compute_lesson_count",
        help="Number of lessons in the course"
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company,
        help="Company associated with the course"
    )
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The course name must be unique.'),
        ('end_date_after_start_date', 'CHECK(end_date >= start_date)', 'End date must be after or equal to start date.'),
    ]
    @api.constrains('capacity')
    def _check_capacity(self):
        for record in self:
            if record.capacity < 0:
                raise UserError("Capacity cannot be negative.")
    def _compute_lesson_count(self):
        for record in self:
            record.lesson_count = self.env['music.school.lesson'].search_count([('course_id', '=', record.id)])
            

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
    
    def action_cancel(self):
        for record in self:
            record.state ='cancelled'
            
    def update_state_in_progress(self):
        for record in self:
            record.state = 'in progress'
    def update_state_draft(self):
        for record in self:
            record.state = 'draft'
    def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]
    def create_lesson(self):
        vals = {
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

    def action_view_lesson(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Lessons',
            'res_model': 'music.school.lesson',
            'view_mode': 'list,form',
            'domain': [('course_id', '=', self.id)],
            'context': {'default_course_id': self.id},
        }

    def finish_courses(self):
        courses = self.env['music.school.course'].search([('state', '!=', 'completed'),('end_date', '<=', fields.Date.today(self))])
        for course in courses:
            course.state = 'completed'
        
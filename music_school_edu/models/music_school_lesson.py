from odoo import models, fields

class MusicSchoolLesson(models.Model):
    _name = "music.school.lesson"
    _description = "Music School Lesson"
    # _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    notes = fields.Html(string="Description", help="Details about the lesson")
    date = fields.Datetime(string="Date", 
            help="Date when the lesson is scheduled",
            default=lambda self: fields.Datetime.now())
    course_id = fields.Many2one(
        comodel_name="music.school.course",
        string="Course",
        help="Course associated with this lesson"
    )
    teacher_id = fields.Many2one(
        comodel_name="music.school.teacher",
        string="Teacher",
        help="Teacher conducting the lesson"
    )
    classroom_id = fields.Many2one(
        comodel_name="music.school.classroom",
        string="Classroom",
        help="Classroom where the lesson takes place"
    )
    color = fields.Integer(
        string="Color",
        help="Color for the lesson in calendar views"
    )
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
    duration = fields.Float(
        string="Duration (hours)",
        help="Duration of the lesson in hours"
    )
    attendace_ids = fields.One2many(
        comodel_name="music.school.lesson.attendance",
        inverse_name="lesson_id",
        string="Attendance Records",
        help="Records of student attendance for this lesson"
    )
    
    def group_expand_state(self, states, domain):
        return [key for key, val in type(self).state.selection]
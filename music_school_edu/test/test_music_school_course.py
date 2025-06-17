from odoo.tests import common

class TestMusicSchoolCourse(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.Course = self.env['music.school.course']
        self.Student = self.env['music.school.student']
        self.Partner = self.env['res.partner']
        self.Lesson = self.env['music.school.lesson']

        self.course_1 = self.Course.create({
            'name': 'Test Course',
            'description': 'This is a test course.',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31',
            'state': 'draft',
        })

        self.course_2 = self.Course.create({
            'name': 'Test Course 2',
            'description': 'This is another test course.',
            'start_date': '2023-02-01',
            'end_date': '2023-11-30',
            'state': 'progress',
        })

        self.lesson_1 = self.Lesson.create({
            'course_id': self.course_1.id,
            'date': '2023-01-15 10:00:00',
            'duration': 2.0,
            'notes': 'First lesson of the course.',
        })
        self.partner_1 = self.Partner.create({
            'name': 'Test Partner 1',
            'email': 'test@gmail.com',
            'phone': '123456789',
        })

        self.partner_2 = self.Partner.create({
            'name': 'Test Partner 2',
            'email': 'test2ŋmail.com',
            'phone': '987654321',
        })

        self.student_1 = self.Student.create({
            'partner_id': self.partner_1.id,
        })

        self.student_2 = self.Student.create({
            'partner_id': self.partner_2.id,
        })
    
    def test_assign_students(self):
        """Test assigning students to a course."""
        self.course_1.assign_students()
        self.assertIn(self.student_1, self.course_1.student_ids)
        self.assertIn(self.student_2, self.course_1.student_ids)
    
    def test_action_finish(self):
        self.course_1.action_finish()
        self.assertEqual(self.course_1.state, 'finished')
        self.assertEqual(self.lesson_1.state, 'done')
    
    def test_create_lesson(self):
        self.course_2.create_lesson()
        lessons = self.Lesson.search([('course_id', '=', self.course_2.id)])
        self.assertTrue(lessons)
from django.test import SimpleTestCase
from resume_form.forms import ResumeForm
from django.core.files.uploadedfile import SimpleUploadedFile

class TestForms(SimpleTestCase):

    def test_resume_form_valid_data(self):
        test_file = SimpleUploadedFile(
            'Test.pdf',
            b'file_content',
            content_type='application/pdf'
        )
        form = ResumeForm(data={
            'name':'test',
            'email':'test@gmail.com',
            'phone':1234,
            'position':'test_position',
            'education':'pos',
            'observations':'none',
        }, files={
            'file':test_file
        })
        
        self.assertTrue(form.is_valid())


    def test_resume_form_no_data(self):
        form = ResumeForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)
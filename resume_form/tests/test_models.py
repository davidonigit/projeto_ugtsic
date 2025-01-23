from resume_form.models import ResumeSubmit
from django.test import TestCase
from django.core.exceptions import ValidationError

class TestModels(TestCase):
    def setUp(self):
        self.submit = ResumeSubmit.objects.create(
            name = 'test',
            email = 'test@gmail.com',
            phone = '1234',
            position = 'test',
            education = 'medio',
            observations = 'none',
            file = '.\curriculos\Test.pdf',
            ip = '1.0.0.1',
        )


    def test_submit_full_clean(self):
        self.assertIsNone(self.submit.full_clean())

    
    def test_submit_name_empty(self):
        self.submit.name = ''
        
        with self.assertRaises(ValidationError) as context:
            self.submit.full_clean()
        
        self.assertIn('Este campo não pode estar vazio.', context.exception.message_dict['name'])
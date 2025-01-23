from django.db import models
from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 1048576
    if file.size > max_size:
        raise ValidationError("O arquivo deve ter no máximo 1MB.")

class ResumeSubmit(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    education = models.CharField(max_length=50, choices=[
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior'),
        ('pos', 'Pós-graduação')
    ])
    observations = models.TextField(blank=True, max_length=100)
    file = models.FileField(upload_to='curriculos/', validators=[validate_file_size])
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.name

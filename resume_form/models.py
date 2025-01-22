from django.db import models
from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 1048576
    if file.size > max_size:
        raise ValidationError("O arquivo deve ter no máximo 1MB.")

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    celphone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    education = models.CharField(max_length=50, choices=[
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('superior', 'Ensino Superior'),
        ('pos', 'Pós-graduação')
    ])
    observations = models.TextField(blank=True)
    file = models.FileField(upload_to='curriculos/', validators=[validate_file_size])

    def __str__(self):
        return self.name
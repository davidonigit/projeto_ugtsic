# Generated by Django 5.1.5 on 2025-01-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumesubmit',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='resumesubmit',
            name='observations',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='resumesubmit',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]

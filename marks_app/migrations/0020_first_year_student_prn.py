# Generated by Django 3.2.5 on 2021-09-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0019_first_year_student_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_year_student',
            name='prn',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 4.2.6 on 2023-10-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0002_course_coursestudent_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
    ]
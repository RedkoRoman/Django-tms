# Generated by Django 4.2.6 on 2023-10-24 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relations.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(through='relations.CourseStudent', to='relations.course'),
        ),
    ]
# Generated by Django 4.2.6 on 2023-11-02 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_infoblog_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoblog',
            name='access_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_book_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/'),
        ),
    ]
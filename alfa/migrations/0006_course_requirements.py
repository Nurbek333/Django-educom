# Generated by Django 5.0.6 on 2024-07-05 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0005_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='requirements',
            field=models.TextField(blank=True, help_text='Enter requirements separated by a newline.'),
        ),
    ]

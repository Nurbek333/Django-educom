# Generated by Django 5.0.6 on 2024-07-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0010_funfact'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images/')),
                ('content', models.TextField()),
            ],
        ),
    ]

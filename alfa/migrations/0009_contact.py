# Generated by Django 5.0.6 on 2024-07-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alfa', '0008_blogpost_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]

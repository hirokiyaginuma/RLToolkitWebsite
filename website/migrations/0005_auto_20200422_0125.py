# Generated by Django 2.2.12 on 2020-04-22 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_tutorials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installing',
            name='author',
        ),
        migrations.RemoveField(
            model_name='installing',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='installing',
            name='published_date',
        ),
    ]

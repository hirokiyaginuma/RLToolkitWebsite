# Generated by Django 2.2.12 on 2020-04-22 09:24

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200422_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installing',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Sample Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Sample Text'),
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Sample Text'),
        ),
    ]

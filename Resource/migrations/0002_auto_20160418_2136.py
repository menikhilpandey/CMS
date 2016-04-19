# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resource', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='bookName',
        ),
        migrations.AlterField(
            model_name='document',
            name='documentType',
            field=models.PositiveIntegerField(choices=[(0, 'Word Document'), (1, 'Text File'), (2, 'Presentation'), (3, 'PDF'), (4, 'Image')]),
        ),
    ]

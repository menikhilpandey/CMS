# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-09 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0012_auto_20160510_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('course', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
            ],
        ),
    ]

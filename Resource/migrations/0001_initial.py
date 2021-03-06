# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-18 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profiler', '0001_initial'),
        ('Course', '0006_auto_20160410_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('name', models.CharField(max_length=250)),
                ('authors', models.CharField(max_length=250)),
                ('edition', models.PositiveIntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('bookType', models.PositiveIntegerField(choices=[(0, 'Text Book'), (1, 'Reference Book')])),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('documentType', models.PositiveIntegerField(choices=[(0, 'Word Document'), (1, 'Text File'), (2, 'Presentation'), (3, 'PDF')])),
                ('source', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('title', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=250)),
                ('publicationDate', models.DateField()),
                ('organization', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WebLink',
            fields=[
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Resource.Resource')),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='course',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Course.Course'),
        ),
        migrations.AddField(
            model_name='resource',
            name='updatedBy',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='Profiler.Faculty'),
        ),
    ]

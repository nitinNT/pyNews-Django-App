# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-13 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('business', 'business'), ('entertainment', 'entertainment'), ('general', 'general'), ('health', 'health'), ('science', 'science'), ('sports', 'sports'), ('technology', 'technology')], max_length=50)),
                ('country', models.CharField(choices=[('in', 'india'), ('us', 'us'), ('jp', 'jp'), ('gr', 'gr')], max_length=50)),
            ],
        ),
    ]

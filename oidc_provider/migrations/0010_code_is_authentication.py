# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oidc_provider", "0009_auto_20160202_1945"),
    ]

    operations = [
        migrations.AddField(
            model_name="code",
            name="is_authentication",
            field=models.BooleanField(default=False),
        ),
    ]

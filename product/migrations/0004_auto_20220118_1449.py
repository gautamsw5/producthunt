# Generated by Django 2.2 on 2022-01-18 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220118_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 18, 14, 49, 52, 18011)),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
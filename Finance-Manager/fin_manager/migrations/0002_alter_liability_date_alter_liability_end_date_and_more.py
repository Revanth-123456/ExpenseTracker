# Generated by Django 4.2.4 on 2023-08-17 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liability',
            name='date',
            field=models.DateField(default=datetime.date(2023, 8, 17)),
        ),
        migrations.AlterField(
            model_name='liability',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liability',
            name='interest_rate',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='liability',
            name='monthly_expense',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]

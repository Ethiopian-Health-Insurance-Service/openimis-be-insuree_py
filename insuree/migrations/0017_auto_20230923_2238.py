# Generated by Django 3.2.16 on 2023-09-23 22:38

import core.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0016_alter_jsonext_column'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsureeStatusReason',
            fields=[
                ('validity_from', core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now)),
                ('validity_to', core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True)),
                ('legacy_id', models.IntegerField(blank=True, db_column='LegacyID', null=True)),
                ('id', models.SmallIntegerField(db_column='StatusReasonId', primary_key=True, serialize=False)),
                ('insuree_status_reason', models.CharField(db_column='StatusReason', max_length=50)),
                ('code', models.CharField(db_column='Code', max_length=5)),
                ('status_type', models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive'), ('DE', 'Dead')], default='AC', max_length=2)),
            ],
            options={
                'db_table': 'tblInsureeStatusReason',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='insuree',
            name='status',
            field=models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive'), ('DE', 'Dead')], default='AC', max_length=2),
        ),
        migrations.AddField(
            model_name='insuree',
            name='status_date',
            field=core.fields.DateField(blank=True, db_column='status_date', null=True),
        ),
        migrations.AddField(
            model_name='insuree',
            name='status_reason',
            field=models.ForeignKey(blank=True, db_column='StatusReason', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='insurees', to='insuree.insureestatusreason'),
        ),
    ]

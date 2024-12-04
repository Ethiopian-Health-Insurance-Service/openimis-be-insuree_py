# Generated by Django 4.2.16 on 2024-11-22 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0023_auto_20240907_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='confirmation_no',
        ),
        migrations.RemoveField(
            model_name='family',
            name='confirmation_type',
        ),
        migrations.RemoveField(
            model_name='family',
            name='family_type',
        ),
        migrations.AddField(
            model_name='family',
            name='household_location',
            field=models.ForeignKey(blank=True, db_column='HouseholdLocationId', related_name='household_families', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.location'), 
        ),
        migrations.AddField(
            model_name='insuree',
            name='household_location',
            field=models.ForeignKey(blank=True, db_column='HouseholdLocationId', related_name='household_insurees', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.location'), 
        ),
    ]
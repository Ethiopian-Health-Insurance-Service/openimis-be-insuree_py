# Generated by Django 4.2.16 on 2024-11-22 11:26

from django.db import migrations, models


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
            name='household_address',
            field=models.CharField(blank=True, db_column='HouseholdAddress', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='insuree',
            name='address',
            field=models.CharField(blank=True, db_column='FamilyAddress', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='insuree',
            name='household_address',
            field=models.CharField(blank=True, db_column='HouseholdAddress', max_length=200, null=True),
        ),
    ]

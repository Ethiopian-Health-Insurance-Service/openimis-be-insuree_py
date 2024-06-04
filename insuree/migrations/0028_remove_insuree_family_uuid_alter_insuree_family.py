# Generated by Django 4.2.11 on 2024-06-04 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insuree', '0027_alter_family_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insuree',
            name='family',
        ),
        migrations.RenameField(
            model_name='insuree',
            old_name='family_uuid',
            new_name='family'
        ),
        migrations.AlterField(
            model_name='insuree',
            name='family',
            field=models.ForeignKey(blank=True, db_column='FamilyUUID', null=True,
                                    on_delete=django.db.models.deletion.DO_NOTHING, to='insuree.family'),
        ),
    ]

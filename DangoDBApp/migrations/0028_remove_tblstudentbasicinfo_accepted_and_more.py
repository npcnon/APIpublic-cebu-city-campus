# Generated by Django 5.0.9 on 2024-09-13 07:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DangoDBApp', '0027_tblstudentbasicinfo_year_level_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tblstudentbasicinfo',
            name='accepted',
        ),
        migrations.AddField(
            model_name='tblstudentbasicinfo',
            name='applicant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentbasicinfoapplications'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1 on 2024-08-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DangoDBApp', '0009_remove_tblstudentacademichistory_ncar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblstudentacademicbackground',
            name='semester_entry',
            field=models.CharField(max_length=20),
        ),
    ]

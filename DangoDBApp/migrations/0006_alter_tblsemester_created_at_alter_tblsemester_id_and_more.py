# Generated by Django 5.0.9 on 2024-10-19 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DangoDBApp', '0005_alter_tblprogram_created_at_alter_tblprogram_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsemester',
            name='created_at',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='tblsemester',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tblsemester',
            name='updated_at',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='tblstudentacademicbackground',
            name='semester_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblsemester'),
        ),
        migrations.AlterField(
            model_name='tblstudentbasicinfo',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblprogram'),
        ),
    ]

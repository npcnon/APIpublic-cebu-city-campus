# Generated by Django 5.0.9 on 2024-10-13 10:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DangoDBApp', '0005_rename_active_tblbugreport_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbldepartment',
            old_name='department_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='tbldepartment',
            old_name='department_dean',
            new_name='dean',
        ),
        migrations.RenameField(
            model_name='tbldepartment',
            old_name='department_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tblprogram',
            old_name='program',
            new_name='description',
        ),
        migrations.AlterUniqueTogether(
            name='tbldepartment',
            unique_together={('name', 'campus_id', 'code', 'dean')},
        ),
        migrations.AlterUniqueTogether(
            name='tblprogram',
            unique_together={('description', 'department_id')},
        ),
        migrations.AddField(
            model_name='tblbugreport',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblbugreport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tblcampus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tblcampus',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tblcampus',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblcampus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tbldepartment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbldepartment',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tbldepartment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tblprogram',
            name='code',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tblprogram',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tblprogram',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblprogram',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tblstudentacademicbackground',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblstudentacademichistory',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblstudentaddpersonaldata',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblstudentbasicinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblstudentfamilybackground',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblstudentofficialinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tblstudentpersonaldata',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

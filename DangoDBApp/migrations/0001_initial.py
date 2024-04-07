# Generated by Django 5.0.3 on 2024-04-05 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblDepartment',
            fields=[
                ('department_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblRoomInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=255)),
                ('floor_lvl', models.CharField(max_length=255)),
                ('room_no', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblSomething',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblStdntInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('m_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('birth_date', models.DateTimeField()),
                ('gender', models.CharField(max_length=255)),
                ('civil_stat', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentPersonalData',
            fields=[
                ('student_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('birth_place', models.CharField(max_length=255)),
                ('marital_status', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=50)),
                ('acr', models.CharField(max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user_level', models.CharField(max_length=255)),
                ('user_role', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('department_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
            ],
        ),
        migrations.CreateModel(
            name='TblStaffInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=255)),
                ('m_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
            ],
        ),
        migrations.CreateModel(
            name='TblAddStaffInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_address', models.TextField()),
                ('contact_info', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstaffinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TblStdntSchoolDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr_lvl', models.CharField(max_length=255)),
                ('semester', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcourse')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
                ('stdnt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstdntinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentFamilyBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_fname', models.CharField(max_length=50)),
                ('father_mname', models.CharField(max_length=50)),
                ('father_lname', models.CharField(max_length=50)),
                ('father_contact_number', models.CharField(max_length=30)),
                ('father_email', models.EmailField(max_length=254)),
                ('father_occupation', models.TextField()),
                ('father_income', models.TextField()),
                ('father_company', models.TextField()),
                ('mother_fname', models.CharField(max_length=50)),
                ('mother_mname', models.CharField(max_length=50)),
                ('mother_lname', models.CharField(max_length=50)),
                ('mother_contact_number', models.CharField(max_length=30)),
                ('mother_email', models.EmailField(max_length=254)),
                ('mother_occupation', models.TextField()),
                ('mother_income', models.TextField()),
                ('mother_company', models.TextField()),
                ('guardian_fname', models.CharField(max_length=50)),
                ('guardian_mname', models.CharField(max_length=50)),
                ('guardian_lname', models.CharField(max_length=50)),
                ('guardian_relation', models.CharField(max_length=50)),
                ('guardian_contact_number', models.CharField(max_length=30)),
                ('guardian_email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
                ('stdnt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentAcademicHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elementary_school', models.TextField()),
                ('elementary_address', models.TextField()),
                ('elementary_honors', models.TextField()),
                ('elementary_graduate', models.DateTimeField()),
                ('Secondary_school', models.TextField()),
                ('Secondary_address', models.TextField()),
                ('Secondary_honors', models.TextField()),
                ('Secondary_graduate', models.DateTimeField()),
                ('ncar', models.CharField(max_length=50)),
                ('latest_college', models.TextField()),
                ('college_address', models.TextField()),
                ('college_honors', models.TextField()),
                ('course', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('stdnt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentAcademicBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.TextField()),
                ('major_in', models.TextField(null=True)),
                ('student_type', models.CharField(max_length=30)),
                ('semester_entry', models.CharField(max_length=10)),
                ('year_entry', models.DateField()),
                ('year_graduate', models.DateField()),
                ('application_type', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
                ('stdnt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblAddStdntInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_address', models.TextField()),
                ('province_address', models.TextField()),
                ('contact_number', models.CharField(max_length=30)),
                ('city_contact_number', models.CharField(max_length=30)),
                ('province_contact_number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('citizenship', models.CharField(max_length=70)),
                ('active', models.BooleanField(default=True)),
                ('stdnt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblSubjInfo',
            fields=[
                ('offercode', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Description', models.TextField()),
                ('subject_code', models.CharField(max_length=255)),
                ('unit', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcourse')),
            ],
        ),
        migrations.CreateModel(
            name='TblStdntSubj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('stdnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstdntinfo')),
                ('offercode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblsubjinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TblSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_day', models.CharField(max_length=255)),
                ('class_hour', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblroominfo')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstaffinfo')),
                ('offercode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblsubjinfo')),
            ],
        ),
    ]

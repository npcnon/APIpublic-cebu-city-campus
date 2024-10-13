# Generated by Django 5.0.9 on 2024-10-13 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('verification_code', models.CharField(max_length=8)),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TblBugReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_data', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
            ],
            options={
                'unique_together': {('name', 'campus_id', 'code')},
            },
        ),
        migrations.CreateModel(
            name='TblEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('qualifications', models.JSONField(null=True)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=95)),
                ('birth_date', models.DateField()),
                ('contact_number', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
            ],
        ),
        migrations.CreateModel(
            name='TblProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
            ],
            options={
                'unique_together': {('description', 'department_id')},
            },
        ),
        migrations.CreateModel(
            name='TblSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=20)),
                ('school_year', models.CharField(max_length=9)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
            ],
        ),
        migrations.CreateModel(
            name='TblClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblemployee')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblprogram')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblsemester')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentBasicInfo',
            fields=[
                ('basicdata_applicant_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('suffix', models.CharField(blank=True, max_length=100, null=True)),
                ('is_transferee', models.BooleanField()),
                ('year_level', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=11)),
                ('address', models.TextField()),
                ('program', models.CharField(max_length=225)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentPersonalData',
            fields=[
                ('fulldata_applicant_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=100)),
                ('m_name', models.CharField(blank=True, max_length=100, null=True)),
                ('suffix', models.CharField(blank=True, max_length=100, null=True)),
                ('l_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('birth_place', models.TextField()),
                ('marital_status', models.CharField(max_length=7)),
                ('religion', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('acr', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('officially enrolled', 'Officially Enrolled'), ('pending', 'Pending'), ('rejected', 'Rejected'), ('initially enrolled', 'Initially Enrolled')], default='pending', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('basicdata_applicant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_basic_data', to='DangoDBApp.tblstudentbasicinfo')),
            ],
            options={
                'unique_together': {('f_name', 'm_name', 'suffix', 'l_name', 'sex', 'birth_date', 'birth_place', 'marital_status', 'religion', 'country', 'email', 'acr', 'status')},
            },
        ),
        migrations.CreateModel(
            name='TblStudentFamilyBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('father_mname', models.CharField(blank=True, max_length=100, null=True)),
                ('father_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('father_contact_number', models.CharField(blank=True, max_length=30, null=True)),
                ('father_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('father_occupation', models.TextField(blank=True, null=True)),
                ('father_income', models.IntegerField(blank=True, null=True)),
                ('father_company', models.TextField(blank=True, null=True)),
                ('mother_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_mname', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_contact_number', models.CharField(blank=True, max_length=30, null=True)),
                ('mother_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mother_occupation', models.TextField(blank=True, null=True)),
                ('mother_income', models.TextField(blank=True, null=True)),
                ('mother_company', models.TextField(blank=True, null=True)),
                ('guardian_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_mname', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_relation', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_contact_number', models.CharField(blank=True, max_length=30, null=True)),
                ('guardian_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fulldata_applicant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_family_data', to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentAddPersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_address', models.TextField()),
                ('province_address', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(max_length=30)),
                ('city_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('province_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('citizenship', models.CharField(max_length=70)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fulldata_applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_addpersonal_data', to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentAcademicHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elementary_school', models.TextField(default='Not Provided')),
                ('elementary_address', models.TextField(default='Not Provided')),
                ('elementary_honors', models.TextField(blank=True, default='None', null=True)),
                ('elementary_graduate', models.IntegerField(blank=True, null=True)),
                ('junior_highschool', models.TextField(default='Not Provided')),
                ('junior_address', models.TextField(default='Not Provided')),
                ('junior_honors', models.TextField(blank=True, default='None', null=True)),
                ('junior_graduate', models.IntegerField(blank=True, null=True)),
                ('senior_highschool', models.TextField(default='Not Provided')),
                ('senior_address', models.TextField(default='Not Provided')),
                ('senior_honors', models.TextField(blank=True, default='None', null=True)),
                ('senior_graduate', models.IntegerField(blank=True, null=True)),
                ('ncae_grade', models.CharField(blank=True, default='Unknown', max_length=50, null=True)),
                ('ncae_year_taken', models.IntegerField(blank=True, null=True)),
                ('latest_college', models.TextField(blank=True, default='Not Provided', null=True)),
                ('college_address', models.TextField(blank=True, default='Not Provided', null=True)),
                ('college_honors', models.TextField(blank=True, default='None', null=True)),
                ('program', models.TextField(blank=True, default='Not Specified', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fulldata_applicant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_academichistory_data', to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentAcademicBackground',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_in', models.TextField(null=True)),
                ('student_type', models.CharField(max_length=30)),
                ('semester_entry', models.CharField(max_length=20)),
                ('year_entry', models.IntegerField()),
                ('year_level', models.CharField(max_length=8)),
                ('year_graduate', models.IntegerField()),
                ('application_type', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblprogram')),
                ('fulldata_applicant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_academicbackground_data', to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblStudentOfficialInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
                ('fulldata_applicant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
            options={
                'unique_together': {('campus', 'student_id')},
            },
        ),
    ]

# Generated by Django 5.0.9 on 2024-09-28 13:33

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
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblCampus',
            fields=[
                ('name', models.CharField(max_length=225, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TblDepartment',
            fields=[
                ('department_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblGradingPeriod',
            fields=[
                ('period_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
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
            name='TblStudentPersonalData',
            fields=[
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
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblStudentPersonalDataApplications',
            fields=[
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
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('applicant_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
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
            name='TblProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=255)),
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
            name='TblSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_day', models.CharField(max_length=255)),
                ('class_hour_start', models.CharField(max_length=255)),
                ('class_hour_end', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblroominfo')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstaffinfo')),
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
            name='TblStdntSubjEnrolled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('Schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblschedule')),
                ('stdnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
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
                ('year_graduate', models.IntegerField()),
                ('application_type', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblprogram')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblStudentBasicInfoApplications',
            fields=[
                ('applicant_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
            ],
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
                ('active', models.BooleanField(default=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
            options={
                'abstract': False,
            },
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
                ('active', models.BooleanField(default=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblStudentAcademicBackgroundApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_in', models.TextField(null=True)),
                ('student_type', models.CharField(max_length=30)),
                ('semester_entry', models.CharField(max_length=20)),
                ('year_entry', models.IntegerField()),
                ('year_graduate', models.IntegerField()),
                ('application_type', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbldepartment')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblprogram')),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblGrades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('active', models.BooleanField(default=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tbladdstaffinfo')),
                ('grading_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblgradingperiod')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstdntsubjenrolled')),
                ('semester_and_academicyr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentacademicbackground')),
                ('stdnt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
        ),
        migrations.CreateModel(
            name='TblAddPersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_address', models.TextField()),
                ('province_address', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(max_length=30)),
                ('city_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('province_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('citizenship', models.CharField(max_length=70)),
                ('active', models.BooleanField(default=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldata')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblStudentFamilyBackgroundApplications',
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
                ('active', models.BooleanField(default=True)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldataapplications')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblStudentAcademicHistoryApplications',
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
                ('active', models.BooleanField(default=True)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldataapplications')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblAddPersonalDataApplications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_address', models.TextField()),
                ('province_address', models.TextField(blank=True, null=True)),
                ('contact_number', models.CharField(max_length=30)),
                ('city_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('province_contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('citizenship', models.CharField(max_length=70)),
                ('active', models.BooleanField(default=True)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentpersonaldataapplications')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TblSubjInfo',
            fields=[
                ('offercode', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Description', models.TextField()),
                ('subject_code', models.CharField(max_length=255)),
                ('unit', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblprogram')),
            ],
        ),
        migrations.AddField(
            model_name='tblstdntsubjenrolled',
            name='offercode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblsubjinfo'),
        ),
        migrations.AddField(
            model_name='tblschedule',
            name='offercode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblsubjinfo'),
        ),
        migrations.CreateModel(
            name='TblStudentBasicInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblcampus')),
                ('applicant_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DangoDBApp.tblstudentbasicinfoapplications')),
            ],
            options={
                'unique_together': {('campus', 'student_id')},
            },
        ),
    ]

# Generated by Django 5.0.9 on 2024-10-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DangoDBApp', '0007_alter_tblstudentaddpersonaldata_fulldata_applicant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblstudentofficialinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tblstudentofficialinfo',
            name='student_id',
            field=models.CharField(max_length=10),
        ),
    ]

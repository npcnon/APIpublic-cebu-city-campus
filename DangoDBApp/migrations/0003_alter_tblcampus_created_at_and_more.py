# Generated by Django 5.0.9 on 2024-10-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DangoDBApp', '0002_alter_tblcampus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblcampus',
            name='created_at',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='tblcampus',
            name='updated_at',
            field=models.CharField(max_length=225),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_dashboard', '0002_alter_studentmodel_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='enrollment',
            field=models.CharField(max_length=12, null=True),
        ),
    ]

# Generated by Django 5.1.2 on 2024-12-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmodel',
            name='year',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
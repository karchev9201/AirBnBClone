# Generated by Django 2.2.5 on 2020-07-01 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200701_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('canceld', 'Canceld'), ('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]

# Generated by Django 2.2.5 on 2020-07-03 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20200701_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceld', 'Canceld'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]

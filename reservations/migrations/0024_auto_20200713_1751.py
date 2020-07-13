# Generated by Django 2.2.5 on 2020-07-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0023_auto_20200712_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceld', 'Canceld')], default='pending', max_length=12),
        ),
    ]
# Generated by Django 2.2.5 on 2020-07-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0021_auto_20200712_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceld', 'Canceld'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]

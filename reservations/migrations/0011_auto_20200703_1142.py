# Generated by Django 2.2.5 on 2020-07-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0010_auto_20200703_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('canceld', 'Canceld'), ('pending', 'Pending'), ('confirmed', 'Confirmed')], default='pending', max_length=12),
        ),
    ]

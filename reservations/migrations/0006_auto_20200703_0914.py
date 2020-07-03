# Generated by Django 2.2.5 on 2020-07-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20200703_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('canceld', 'Canceld'), ('pending', 'Pending')], default='pending', max_length=12),
        ),
    ]
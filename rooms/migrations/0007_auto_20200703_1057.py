# Generated by Django 2.2.5 on 2020-07-03 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200703_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
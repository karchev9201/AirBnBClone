# Generated by Django 2.2.5 on 2020-07-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200712_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('email', 'Email'), ('github', 'Github'), ('kakako', 'KAKAO')], default='usd', max_length=3),
        ),
    ]

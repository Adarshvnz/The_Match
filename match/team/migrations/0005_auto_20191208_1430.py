# Generated by Django 2.2.6 on 2019-12-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_team_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='confirm',
            field=models.BooleanField(default=True),
        ),
    ]

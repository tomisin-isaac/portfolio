# Generated by Django 3.2.4 on 2021-06-30 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_job',
            field=models.CharField(default='WEB DEVELOPER', max_length=30),
        ),
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(default='Tomisin Isaac', max_length=30),
        ),
    ]

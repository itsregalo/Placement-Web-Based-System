# Generated by Django 3.2.8 on 2022-05-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220528_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

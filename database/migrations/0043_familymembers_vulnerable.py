# Generated by Django 4.2.5 on 2023-12-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0042_familymembers_deniedby'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymembers',
            name='vulnerable',
            field=models.BooleanField(default=False),
        ),
    ]

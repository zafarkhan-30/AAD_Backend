# Generated by Django 4.2.5 on 2023-12-07 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0048_alter_familymembers_vulnerable_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='supervisor',
            new_name='careated_by',
        ),
    ]

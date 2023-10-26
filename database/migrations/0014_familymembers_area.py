# Generated by Django 4.2.5 on 2023-10-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_rename_area_area_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymembers',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familymembers_area', to='database.area'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0029_merge_20231106_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='labtests',
            name='testId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
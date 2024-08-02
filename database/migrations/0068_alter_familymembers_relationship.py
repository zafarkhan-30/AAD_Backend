# Generated by Django 4.2.4 on 2024-06-10 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0067_familymembers_casecompletion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymembers',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Self', 'Self'), ('Mother', 'Mother'), ('Father', 'Father'), ('Spouse', 'Spouse'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Grandson', 'Grandson'), ('Granddaughter', 'Granddaughter'), ('Grandmother', 'Grandmother'), ('Grandfather', 'Grandfather'), ('Uncle', 'Uncle'), ('Aunty', 'Aunty'), ('Nephew', 'Nephew'), ('Niece', 'Niece'), ('Sibling', 'Sibling')], max_length=100, null=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-03-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0032_rename_cabform_cabdetailform'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabdetailform',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]

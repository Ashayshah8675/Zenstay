# Generated by Django 5.0.1 on 2024-03-19 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0034_eventdetailform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetailform',
            name='ename',
        ),
    ]
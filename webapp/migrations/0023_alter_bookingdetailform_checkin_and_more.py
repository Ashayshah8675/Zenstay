# Generated by Django 5.0.1 on 2024-02-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_alter_bookingdetailform_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetailform',
            name='checkin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bookingdetailform',
            name='checkout',
            field=models.DateField(null=True),
        ),
    ]

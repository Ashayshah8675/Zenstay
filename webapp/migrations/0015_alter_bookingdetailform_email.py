# Generated by Django 5.0.1 on 2024-02-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_rename_bookingdetail_bookingdetailform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetailform',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]

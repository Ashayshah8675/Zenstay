# Generated by Django 5.0.1 on 2024-02-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_services_alter_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='images\\Testimonial'),
        ),
    ]

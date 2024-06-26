# Generated by Django 5.0.1 on 2024-02-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_services_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='explore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/Service')),
            ],
        ),
    ]

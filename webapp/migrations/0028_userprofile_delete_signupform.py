# Generated by Django 5.0.1 on 2024-02-29 09:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_alter_signupform_password_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='signupform',
        ),
    ]

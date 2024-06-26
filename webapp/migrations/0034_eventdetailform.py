# Generated by Django 5.0.1 on 2024-03-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0033_cabdetailform_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='eventdetailform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('people', models.IntegerField()),
                ('request', models.TextField()),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]

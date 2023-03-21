# Generated by Django 4.1.3 on 2022-11-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50)),
                ('patient_name', models.CharField(max_length=50)),
                ('doctor_username', models.CharField(max_length=50)),
                ('pateint_username', models.CharField(max_length=50)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
                ('prescription', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('specialization', models.CharField(max_length=50)),
            ],
        ),
    ]
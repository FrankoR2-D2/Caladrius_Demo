# Generated by Django 4.0.5 on 2022-07-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(null=True, verbose_name='Start time')),
                ('end_time', models.TimeField(null=True, verbose_name='End time')),
                ('date', models.DateField(null=True, verbose_name='Date')),
                ('status', models.BooleanField(null=True, verbose_name='Appointment Status')),
                ('appointment_reason', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('General Practioner', 'General Practioner'), ('Anesthesiologists', 'Anesthesiologists'), ('Dermatologists', 'Dermatologists'), ('Family Physician', 'Family Physician'), ('Internists', 'Internists'), ('Pediatrician', 'Pediatrician'), ('Radiologists', 'Radiologists'), ('Cardiologist', 'Cardiologist'), ('Audiologist', 'Audiologist')], default='GP', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('complete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientNotes', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]

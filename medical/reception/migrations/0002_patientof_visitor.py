# Generated by Django 5.1.1 on 2024-12-19 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illness', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_relationships', to='reception.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_relationships', to='reception.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('visitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('visitor_tc', models.IntegerField(unique=True)),
                ('visitor_name', models.CharField(max_length=50)),
                ('visitor_surname', models.CharField(max_length=50)),
                ('patient_closeness', models.CharField(max_length=50)),
                ('patient_room', models.IntegerField()),
                ('visitor_entry_time', models.TimeField()),
                ('visitor_exit_time', models.TimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to='reception.patient')),
            ],
        ),
    ]

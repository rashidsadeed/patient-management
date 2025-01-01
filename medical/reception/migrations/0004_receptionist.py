# Generated by Django 5.1.1 on 2024-12-24 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0003_remove_doctor_doc_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('emp_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='reception.employee')),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
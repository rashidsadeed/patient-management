# Generated by Django 5.1.1 on 2024-12-19 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_patientof_visitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doc_name',
        ),
    ]
# Generated by Django 5.1.2 on 2024-12-24 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0005_alter_student_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='student',
            table='admission_student',
        ),
    ]
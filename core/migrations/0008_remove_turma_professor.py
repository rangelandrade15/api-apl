# Generated by Django 5.1.4 on 2024-12-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_professor_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='professor',
        ),
    ]

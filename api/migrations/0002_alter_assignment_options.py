# Generated by Django 3.2.13 on 2022-08-08 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'ordering': ['-dt']},
        ),
    ]

# Generated by Django 4.1.2 on 2022-12-11 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_accessrequest_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrequest',
            old_name='file',
            new_name='signature',
        ),
    ]

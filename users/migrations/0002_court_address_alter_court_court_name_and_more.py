# Generated by Django 4.1.2 on 2022-10-31 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='court',
            name='court_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='court',
            name='governor',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# Generated by Django 2.1.4 on 2019-01-29 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20190125_1444'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tblbank',
            unique_together=set(),
        ),
    ]

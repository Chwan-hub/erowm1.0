# Generated by Django 2.0.13 on 2020-04-30 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0028_business_session_month'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subdivision',
            unique_together={('business', 'item', 'code')},
        ),
    ]
# Generated by Django 2.1.4 on 2020-02-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0026_auto_20200226_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='enable',
            field=models.CharField(default='Y', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paragraph',
            name='enable',
            field=models.CharField(default='Y', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subsection',
            name='enable',
            field=models.CharField(default='Y', max_length=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200422_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subj1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='subj2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='subj3',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 3.2.20 on 2023-07-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_alter_personmodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='age',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
# Generated by Django 2.2.4 on 2020-11-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20201110_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
    ]

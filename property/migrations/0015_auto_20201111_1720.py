# Generated by Django 2.2.4 on 2020-11-11 14:20

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20201111_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owners_phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]

# Generated by Django 2.2.4 on 2020-11-10 07:46

from django.db import migrations


def calculate_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
            flat.save()
        else:
            flat.new_building = False
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(calculate_new_building)
    ]

# Generated by Django 2.2.4 on 2020-11-11 11:15

from django.db import migrations


def flat_owner_relation(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            owner=flat.owner,
            owner_pure_phone=flat.owner_pure_phone,
            owners_phonenumber=flat.owners_phonenumber,
        )
        flat.owners.set([owner])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20201110_1706'),
    ]

    operations = [
        migrations.RunPython(flat_owner_relation)
    ]

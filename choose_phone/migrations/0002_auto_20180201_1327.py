# Generated by Django 2.0.1 on 2018-02-01 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('choose_phone', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phones',
            new_name='Phone',
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'Номера телефонов'},
        ),
    ]
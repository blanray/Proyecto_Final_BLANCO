# Generated by Django 5.0.7 on 2024-08-10 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='nombre',
            new_name='name',
        ),
    ]

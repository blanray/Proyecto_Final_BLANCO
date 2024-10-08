# Generated by Django 5.0.7 on 2024-08-10 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_rename_nombre_book_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portadas')),
                ('book', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Books.book')),
            ],
        ),
    ]

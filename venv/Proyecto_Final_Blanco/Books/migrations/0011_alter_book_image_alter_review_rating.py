# Generated by Django 5.0.7 on 2024-08-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0010_rename_comentario_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='portadas'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
        ),
    ]

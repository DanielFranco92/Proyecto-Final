# Generated by Django 5.0.1 on 2024-02-12 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='comentario',
        ),
    ]

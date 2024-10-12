# Generated by Django 5.1.1 on 2024-10-11 05:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='usuario',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='fecha_creacion',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-02-09 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0005_alter_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='URL de Imagen'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='facebook',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Facebook de Autor'),
        ),
        migrations.AddField(
            model_name='autor',
            name='instagram',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Instagram de Autor'),
        ),
        migrations.AddField(
            model_name='autor',
            name='twitter',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Twitter de Autor'),
        ),
    ]

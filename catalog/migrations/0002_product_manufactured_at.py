# Generated by Django 5.0.4 on 2024-05-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateField(default='2024', verbose_name='Дата производства'),
        ),
    ]

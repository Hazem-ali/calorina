# Generated by Django 3.1.7 on 2024-01-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20240116_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='saturated_fat',
        ),
        migrations.RemoveField(
            model_name='item',
            name='trans_fat',
        ),
        migrations.AddField(
            model_name='item',
            name='magnesium',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='sugars',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
    ]

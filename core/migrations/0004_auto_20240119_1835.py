# Generated by Django 3.1.7 on 2024-01-19 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20240119_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='carbohydrates',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='cholesterol',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='fiber',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='magnesium',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='protein',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='sodium',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='sugars',
            field=models.DecimalField(decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_fat',
            field=models.DecimalField(decimal_places=4, max_digits=6),
        ),
    ]

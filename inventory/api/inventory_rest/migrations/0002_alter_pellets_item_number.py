# Generated by Django 4.0.3 on 2024-02-16 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pellets',
            name='item_number',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]

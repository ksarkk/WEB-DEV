# Generated by Django 5.0.4 on 2024-04-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_product_category_product_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_product_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(),
        ),
    ]

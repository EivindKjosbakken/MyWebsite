# Generated by Django 4.0.1 on 2022-01-31 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_price_alter_product_summary_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='summary',
        ),
    ]

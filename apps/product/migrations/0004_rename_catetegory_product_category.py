# Generated by Django 5.1.5 on 2025-04-19 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_name_alter_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catetegory',
            new_name='category',
        ),
    ]

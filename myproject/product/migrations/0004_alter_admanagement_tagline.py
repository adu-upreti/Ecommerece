# Generated by Django 5.0.7 on 2024-08-01 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_category_admanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admanagement',
            name='tagline',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]

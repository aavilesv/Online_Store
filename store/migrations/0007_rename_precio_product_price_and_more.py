# Generated by Django 4.0.4 on 2022-05-19 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customer_create_date_alter_order_order_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='precio',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 22, 6, 25, 47194), verbose_name='fecha de registro'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 22, 6, 25, 48193)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 22, 6, 25, 48193)),
        ),
    ]

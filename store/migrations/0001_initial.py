# Generated by Django 4.0.4 on 2022-05-19 21:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(default='', max_length=200, verbose_name='Nombre')),
                ('first_name', models.CharField(default='', max_length=200, verbose_name='DIRECCION')),
                ('last_name', models.CharField(default='', max_length=200, verbose_name='sitio web')),
                ('email', models.CharField(default='', max_length=200, verbose_name='Email')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 21, 31, 15, 392203), verbose_name='fecha de registro')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 21, 31, 15, 393203))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Order',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 19, 21, 31, 15, 393203))),
                ('code', models.CharField(default=' ', max_length=200)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.order')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='store.product')),
            ],
            options={
                'verbose_name': 'Order_detail',
                'verbose_name_plural': 'Order_details',
                'ordering': ['id'],
            },
        ),
    ]

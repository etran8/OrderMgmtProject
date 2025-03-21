# Generated by Django 2.1.11 on 2021-02-22 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OrderMgmtApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=11)),
                ('created_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='OrderMgmtApp.Customer')),
            ],
            options={
                'ordering': ['street'],
            },
        ),
        migrations.CreateModel(
            name='CustomerX',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('premium_customer', models.BooleanField()),
                ('reliability_rating', models.IntegerField()),
                ('customer_since', models.DateField(auto_now=True)),
                ('cell_phone', models.CharField(max_length=15)),
                ('home_phone', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(max_length=10)),
                ('payment_method', models.CharField(max_length=10)),
                ('payment_acct_number', models.CharField(max_length=20)),
                ('payment_acct_security_code', models.IntegerField(max_length=5)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='OrderMgmtApp.Customer')),
            ],
            options={
                'ordering': ['customer'],
            },
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(max_length=2)),
                ('created_date', models.DateField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='OrderMgmtApp.Order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]

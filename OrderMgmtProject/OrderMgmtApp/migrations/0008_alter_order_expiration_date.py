# Generated by Django 5.0.1 on 2024-05-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderMgmtApp', '0007_alter_customer_customer_since_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiration_date',
            field=models.DateField(default=2025),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-21 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_customer_customermultipleproduct_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customermultipleproduct',
            old_name='customer_name',
            new_name='customer',
        ),
    ]
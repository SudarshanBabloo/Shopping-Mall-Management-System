# Generated by Django 2.2 on 2019-04-14 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0009_auto_20190414_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='7922010BAF34', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADDB6AB2DFB3', max_length=14),
        ),
    ]

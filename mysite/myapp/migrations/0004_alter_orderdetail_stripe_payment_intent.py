# Generated by Django 4.2.23 on 2025-06-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_stripe_payment_intent_id_orderdetail_stripe_payment_intent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='stripe_payment_intent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_account_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

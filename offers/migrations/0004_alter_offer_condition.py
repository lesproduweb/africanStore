# Generated by Django 3.2.4 on 2021-07-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0003_auto_20210710_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='condition',
            field=models.CharField(choices=[('bon état', 'Bon état')], default='shop', max_length=120),
        ),
    ]
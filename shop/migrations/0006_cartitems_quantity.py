# Generated by Django 5.1.2 on 2024-11-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

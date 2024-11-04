# Generated by Django 5.1.2 on 2024-10-29 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_seller_seller_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_status',
            field=models.CharField(choices=[('S', 'Suspended'), ('N', 'NO'), ('B', 'Blocked'), ('Y', 'YES')], max_length=1),
        ),
    ]
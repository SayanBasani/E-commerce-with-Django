# Generated by Django 5.1.2 on 2024-10-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_customuser_alter_seller_seller_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_status',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO'), ('B', 'Blocked'), ('S', 'Suspended')], max_length=1),
        ),
    ]

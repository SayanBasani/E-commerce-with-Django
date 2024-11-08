# Generated by Django 5.1.2 on 2024-10-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_seller_admin_userprofile'),
        ('shop', '0003_alter_shop_items_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='seller_models',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='email',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='password',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='username',
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_status',
            field=models.CharField(choices=[('Y', 'YES'), ('N', 'NO'), ('B', 'Blocked'), ('S', 'Suspended')], default=' ', max_length=1),
            preserve_default=False,
        ),
    ]

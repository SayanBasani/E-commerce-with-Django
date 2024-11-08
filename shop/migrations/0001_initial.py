# Generated by Django 5.1.2 on 2024-10-29 02:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0006_alter_seller_seller_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='seller_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.TextField(max_length=150)),
                ('item_others_details', models.JSONField()),
                ('upload_datetime', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_items', to='account.seller')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shopping_items/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.seller_product')),
            ],
        ),
        migrations.CreateModel(
            name='item_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_datetime', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('commented_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='shop.seller_product')),
            ],
        ),
    ]

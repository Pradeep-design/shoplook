# Generated by Django 3.0.4 on 2021-05-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
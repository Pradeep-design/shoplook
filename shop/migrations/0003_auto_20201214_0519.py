# Generated by Django 3.0.4 on 2020-12-14 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_ue'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='Ue',
        ),
    ]

# Generated by Django 3.0.4 on 2021-06-16 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210615_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]

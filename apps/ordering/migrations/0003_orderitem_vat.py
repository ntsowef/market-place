# Generated by Django 3.2.4 on 2021-12-31 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]

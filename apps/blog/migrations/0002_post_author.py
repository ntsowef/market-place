# Generated by Django 3.2.4 on 2022-01-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.4 on 2022-02-12 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author_detail',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0002_rename_carma_author_rating_rename_head_post_header_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_of_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

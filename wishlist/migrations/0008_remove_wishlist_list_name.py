# Generated by Django 3.0.2 on 2020-01-29 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0007_remove_wishlist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='list_name',
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-07 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_profile_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='favorites',
            new_name='favourites',
        ),
    ]
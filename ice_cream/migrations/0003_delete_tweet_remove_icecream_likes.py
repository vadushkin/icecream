# Generated by Django 4.0.6 on 2022-07-15 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_tweet_alter_icecream_options_remove_icecream_views_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tweet',
        ),
        migrations.RemoveField(
            model_name='icecream',
            name='likes',
        ),
    ]
# Generated by Django 3.1.4 on 2021-07-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0009_remove_post_subheading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url_field',
            field=models.URLField(blank=True, default='URLInput', max_length=300),
        ),
    ]
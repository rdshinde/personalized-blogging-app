# Generated by Django 3.1.4 on 2021-07-04 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0014_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
    ]

# Generated by Django 3.1.4 on 2021-07-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0003_post_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='TextInput', max_length=200, unique=True),
        ),
    ]
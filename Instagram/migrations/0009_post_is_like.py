# Generated by Django 3.2.9 on 2022-10-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0008_post_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-22 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chargebacks', '0007_comment_created_at_comment_dislikes_comment_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
    ]

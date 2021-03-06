# Generated by Django 2.2.7 on 2019-12-05 20:33

import django.db.models.deletion
from django.db import migrations
from django.db import models

import pitter.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                (
                    'id',
                    models.CharField(
                        default=pitter.models.base.default_uuid_id,
                        editable=False,
                        max_length=256,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fake_id', models.CharField(default='', max_length=50)),
                ('message', models.CharField(max_length=256)),
                ('user_comment', models.TextField()),
            ],
            options={'abstract': False,},
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                (
                    'id',
                    models.CharField(
                        default=pitter.models.base.default_uuid_id,
                        editable=False,
                        max_length=256,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('login', models.CharField(max_length=32, unique=True)),
                ('hash_of_password_with_salt', models.BinaryField(max_length=32)),
                ('salt_for_password', models.BinaryField(max_length=16)),
                ('email_address', models.CharField(blank=True, max_length=254)),
                ('email_notifications_enabled', models.BooleanField()),
                ('name', models.CharField(blank=True, max_length=32)),
            ],
            options={'abstract': False,},
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                (
                    'id',
                    models.CharField(
                        default=pitter.models.base.default_uuid_id,
                        editable=False,
                        max_length=256,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'follower',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='following', to='pitter.User'
                    ),
                ),
                (
                    'following',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='pitter.User'
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name='follower',
            constraint=models.UniqueConstraint(
                fields=('follower', 'following'), name='uniqueness_of_follower-following_pair'
            ),
        ),
    ]

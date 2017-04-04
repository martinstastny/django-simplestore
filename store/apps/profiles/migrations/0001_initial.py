# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(verbose_name='Last Name', max_length=100)),
                ('slug', models.SlugField()),
                ('updated', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, to='auth.Permission', related_name='user_set', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

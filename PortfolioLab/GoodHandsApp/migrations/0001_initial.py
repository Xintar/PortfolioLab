# Generated by Django 4.0.2 on 2024-01-19 08:56

import GoodHandsApp.models
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', GoodHandsApp.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('description', models.TextField(verbose_name='Opis')),
                ('type', models.FloatField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], default=1, verbose_name='Instytucja')),
                ('categories', models.ManyToManyField(to='GoodHandsApp.Category', verbose_name='Kategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Liczba worków')),
                ('address', models.CharField(max_length=255, verbose_name='Adres')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Numer telefonu')),
                ('city', models.CharField(max_length=255, verbose_name='Miasto')),
                ('zip_code', models.CharField(max_length=20, verbose_name='Kod pocztowy')),
                ('pick_up_date', models.DateTimeField(verbose_name='Data odbioru')),
                ('pick_up_time', models.DateTimeField(verbose_name='Czas odbioru')),
                ('pick_up_comment', models.TextField(verbose_name='Komentarz do odbioru')),
                ('categories', models.ManyToManyField(to='GoodHandsApp.Category', verbose_name='Kategoria')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GoodHandsApp.institution', verbose_name='Instytucja')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Darczyńca')),
            ],
        ),
    ]

from django.contrib.auth.models import (
    AbstractUser,
    UserManager
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from PortfolioLab import settings


class MyUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Adres email jest wymagany')
        username = email

        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Adres email jest wymagany')
        username = email

        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Nazwa"
    )


class Institution(models.Model):
    TYPE_CHOICES = (
        (1, "fundacja"),
        (2, "organizacja pozarządowa"),
        (3, "zbiórka lokalna")
    )

    name = models.CharField(
        max_length=255,
        verbose_name="Nazwa"
    )
    description = models.TextField(
        verbose_name="Opis"
    )
    type = models.FloatField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name="Instytucja"
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name="Kategoria"
    )


class Donation(models.Model):
    quantity = models.IntegerField(
        verbose_name="Liczba worków"
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name="Kategoria"
    )
    institution = models.ForeignKey(
        Institution,
        on_delete=models.CASCADE,
        verbose_name="Instytucja"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Adres"
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Numer telefonu"
    )
    city = models.CharField(
        max_length=255,
        verbose_name="Miasto"
    )
    zip_code = models.CharField(
        max_length=20,
        verbose_name="Kod pocztowy"
    )
    pick_up_date = models.DateTimeField(
        verbose_name="Data odbioru"
    )
    pick_up_time = models.DateTimeField(
        verbose_name="Czas odbioru"
    )
    pick_up_comment = models.TextField(
        verbose_name="Komentarz do odbioru"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        blank=True,
        verbose_name="Darczyńca"
    )

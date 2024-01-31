from django.contrib.auth.models import (
    AbstractUser,
    UserManager as DjangoUserManager
)
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.translation import gettext_lazy as _

from PortfolioLab import settings


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = UserManager()

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
    pick_up_date = models.DateField(
        verbose_name="Data odbioru"
    )
    pick_up_time = models.TimeField(
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

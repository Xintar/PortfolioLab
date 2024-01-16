from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin, User
)
from django.db import models
from django.utils import timezone

from PortfolioLab import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Adres email jest wymagany')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


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

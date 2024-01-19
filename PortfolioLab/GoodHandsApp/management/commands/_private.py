from faker import Factory

from GoodHandsApp.models import (
    Category,
    Institution,
    Donation
)
from random import randint


CATEGORIES = (
    "ubrania",
    "jedzenie",
    "sprzęt AGD",
    "meble",
    "zabawki",
    "ciepłe koce"
)


def create_category():

    for categori in CATEGORIES:
        Category.objects.create(name=categori)


def create_institution():
    fake = Factory.create("pl_PL")

    for _ in range(5):
        for institution in range(1, 4):
            i = Institution.objects.create(
                name=(Institution.TYPE_CHOICES[institution - 1][1]).capitalize(),
                description=fake.sentence(),
                type=institution,
            )

            cat = []
            for _ in range(randint(1, Category.objects.all().count())):
                cat.append(randint(1, Category.objects.all().count()))

            cat = list(set(cat))

            for category in cat:
                c = Category.objects.get(name=CATEGORIES[category - 1])
                i.categories.add(c)
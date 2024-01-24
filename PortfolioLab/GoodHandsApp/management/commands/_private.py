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


def add_related_category(model_name):
    cat = []
    for _ in range(randint(1, Category.objects.all().count())):
        cat.append(randint(1, Category.objects.all().count()))

    cat = list(set(cat))

    for category in cat:
        c = Category.objects.get(name=CATEGORIES[category - 1])
        model_name.categories.add(c)


def create_institution():
    fake = Factory.create("pl_PL")

    for _ in range(5):
        for institution in range(1, 4):
            i = Institution.objects.create(
                name=(Institution.TYPE_CHOICES[institution - 1][1]).capitalize(),
                description=fake.sentence(),
                type=institution,
            )

            add_related_category(i)


def create_donation():
    fake = Factory.create("pl_PL")

    institutions = Institution.objects.all()

    for institution in institutions:
        for _ in range(0, randint(0, 5)):
            d = Donation.objects.create(
                quantity=randint(1, 10),
                institution=institution,
                address=fake.address(),
                phone_number=fake.phone_number(),
                city=fake.city(),
                zip_code=fake.postcode(),
                pick_up_date=fake.date(),
                pick_up_time=fake.time(),
                pick_up_comment=fake.sentence(),
            )

            add_related_category(d)

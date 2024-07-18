from faker import Factory

from GoodHandsApp.models import (
    Category,
    Institution,
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
    
    numer_institution_to_create =  int(input("Prosze podać ilość instytucji do utworzenia: "))
    
    for _ in range(numer_institution_to_create):
        for institution in range(1, 4):
            if institution == 1:  # Fundacja
                fake_name = f"im. {fake.name()}"
            elif institution == 2:  # Organizacja pozarządowa
                fake_name = f"\"{fake.word()}\""
            else: # Zbiórka lokalna
                fake_name = f"osiedle {fake.city()}"
            
            i = Institution.objects.create(
                name=(f"{Institution.TYPE_CHOICES[institution - 1][1]} {fake_name}").capitalize(),
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

from enum import unique

from models.alcohol import Alcohol
from models.category import Category
from models.metadata import Metadata


def insert_documents(data: list) -> None:
    print('Inserting {} documents'.format(len(data)))
    categories = list()

    def map_alcohols(alcohol: object):
        a = Alcohol(alcohol)
        categories.append(alcohol['categoryLevel1'])
        return a

    alcohols = list(map(map_alcohols, data))

    alcohols.sort(key=lambda x: x.apk, reverse=True)

    # Clear alcohol collection
    Alcohol.objects.delete()

    for alcohol in alcohols:
        alcohol.save()

    # Clear categories collection
    Category.objects.delete()

    unique_categories = get_categories(categories)

    Category.objects.insert(unique_categories)

    # Update metadata
    Metadata.objects.delete()

    meta = Metadata(alcohols_synced=len(alcohols),
                    categories_synced=len(unique_categories))

    meta.save()

    print("{} items inserted, {} categories saved".format(
        len(alcohols), len(unique_categories)))


def get_categories(categories: list):
    unique_categories = list(filter(lambda x: x and x != '', set(categories)))
    return list(map(lambda x: Category(name=x, items=categories.count(x)), unique_categories))

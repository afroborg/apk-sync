from datetime import datetime

from models.alcohol import Alcohol
from models.metadata import Metadata


def insert_documents(data: list) -> None:
    print('Inserting {} documents'.format(len(data)))

    alcohols = list(map(lambda x: Alcohol(x), data))

    alcohols.sort(key=lambda x: x.apk, reverse=True)

    Alcohol.objects.delete()

    for alcohol in alcohols:
        alcohol.save()

    # Update metadata
    meta: Metadata = Metadata.objects.first()

    try:

        if meta:
            meta.last_synced = datetime.now()
            meta.save()
        else:
            Metadata().save()

        print('All {} documents inserted'.format(len(alcohols)))

    except:
        print('Coult not save data to MongoDB')

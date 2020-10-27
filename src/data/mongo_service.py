from datetime import datetime

import mongoengine
from models.alcohol import Alcohol
from models.metadata import Metadata


def insert_documents(data: list) -> None:
    print('Inserting {} documents'.format(len(data)))

    alcohols = list(map(lambda x: Alcohol(x), data))

    Alcohol.objects.delete()

    for alcohol in alcohols:
        alcohol.save()

    # Update metadata
    meta: Metadata = Metadata.objects.first()

    if meta:
        meta.last_synced = datetime.now()
        meta.save()
    else:
        Metadata().save()

    print('All {} documents inserted'.format(len(alcohols)))

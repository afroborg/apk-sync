from datetime import datetime

import mongoengine


class Metadata(mongoengine.Document):
    last_synced = mongoengine.DateTimeField(default=datetime.now)
    alcohols_synced = mongoengine.IntField(min_value=0)
    categories_synced = mongoengine.IntField(min_value=0)

    meta = {
        'db_alias': 'APK',
        'collection': 'metadata'
    }

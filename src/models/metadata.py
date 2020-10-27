import datetime

import mongoengine


class Metadata(mongoengine.Document):
    last_synced: mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'APK',
        'collection': 'metadata'
    }

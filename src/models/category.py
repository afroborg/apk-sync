import mongoengine


class Category(mongoengine.Document):
    name: str = mongoengine.StringField(required=True)
    items: int = mongoengine.IntField(min_value=0)

    meta = {
        'db_alias': 'APK',
        'collection': 'categories'
    }

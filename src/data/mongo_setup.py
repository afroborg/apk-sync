import os

import mongoengine


def global_init():
    alias = 'APK'
    db = os.getenv('MONGO_DB_DATABASE_HOST')
    name = os.getenv('MONGO_DB_DATABASE_NAME')

    mongoengine.register_connection(alias, db, name)

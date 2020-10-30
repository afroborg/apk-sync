import os

import mongoengine


def global_init():
    alias = 'APK'
    db = os.getenv('MONGO_DB_DATABASE_HOST')
    port = os.getenv('MONGO_DB_PORT')
    name = os.getenv('MONGO_DB_DATABASE_NAME')
    username = os.getenv('MONGO_DB_USERNAME')
    password = os.getenv('MONGO_DB_PASSWORD')
    authentication_db = 'admin'

    mongoengine.register_connection(
        alias=alias, db=db, port=int(port), name=name, username=username, password=password, authentication_source=authentication_db)

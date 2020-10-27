import mongoengine


def global_init():
    alias = 'APK'
    db = 'localhost'
    name = 'apk'

    mongoengine.register_connection(alias, db, name)

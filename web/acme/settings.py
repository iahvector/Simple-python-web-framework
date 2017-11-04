from os import environ

MONGO = {
    'HOST': environ.get('MONGO_HOST'),
    'PORT': int(environ.get('MONGO_PORT', '27017')),
    'DB_NAME': environ.get('MONGO_DB_NAME', 'acme'),
    'TEST_DB_NAME': environ.get('MONGO_TEST_DB_NAME', 'acme_test'),
}

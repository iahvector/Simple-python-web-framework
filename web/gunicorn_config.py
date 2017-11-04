import multiprocessing
from os import environ

# Environment variables
PORT = environ.get('PORT')
DEBUG = bool(environ.get('DEBUG', 'False'))

# Binding
bind = "0.0.0.0:{}".format(PORT)

# Workers
workers = multiprocessing.cpu_count() * 2 + 1

# Debugging
reload = DEBUG

# Logging
accesslog = '-'
log_level = 'debug' if DEBUG else 'error'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'myproject',                         # Or path to database file if using sqlite3.
        'USER': 'postgres',                                 # Not used with sqlite3.
        'PASSWORD': 'pwd',                                  # Not used with sqlite3.
        'HOST': 'localhost',                                # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                                     # Set to empty string for default. Not used with sqlite3.
    }
}

SESSION_ENGINE = 'redis_sessions.session'

API_KEY = '$0m3-U/\/1qu3-K3Y'

SEND_MESSAGE_API_URL = 'http://127.0.0.1:8000/messages/send_message_api'

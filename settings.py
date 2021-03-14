from decouple import config

DB_LINK = config("DB_LINK", cast=str)

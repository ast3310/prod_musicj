import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    SECRET_KEY = 'gjh2ggjkg4k2li34b3c12dhgfj321j'
    BASE_URL = os.environ.get('BASE_URL')

class VkConfig:
    TOKEN = os.environ.get('TOKEN')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')


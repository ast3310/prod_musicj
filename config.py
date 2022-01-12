import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    SECRET_KEY = 'gjh2ggjkg4k2li34b3c12dhgfj321j'
    BASE_URL = 'https://127.0.0.1:8080/'

class VkConfig:
    TOKEN = '10eb30398518ec3e3a649e6321048ac843835ec712ae8a1c4ad3ba172319947a437152d0c2ea3b85b6fc5'
    CLIENT_ID = '7379453'
    CLIENT_SECRET = '9s1KTkwODT4DaNqA8DIh'
    USERNAME = '89654893190'
    PASSWORD = 'a909463331a72c24b34e84b0a64502b7'


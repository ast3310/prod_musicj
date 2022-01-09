from flask import Flask
import config as conf 

app = Flask(__name__)
app.config.from_object(conf.BaseConfig)

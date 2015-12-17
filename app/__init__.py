from flask import Flask
from settings import cSettings

app = Flask(__name__)
Settings = cSettings()

from app import views

from flask import Flask
from config import config

app = Flask(__name__)
config(app)

import servusberry.views.webpage
import servusberry.views.files
import servusberry.views.radio
import servusberry.views.transmission

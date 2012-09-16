from config import config
from flask import Flask

app = Flask(__name__)
config(app)

import servusberry.views.webpage
import servusberry.views.files
import servusberry.views.media
import servusberry.views.radio
import servusberry.views.transmission

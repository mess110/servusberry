from flask import Flask

app = Flask(__name__)

import servusberry.views.webpage
import servusberry.views.transmission

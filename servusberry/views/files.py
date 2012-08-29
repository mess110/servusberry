import os

from servusberry import app
from flask import jsonify
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
  def __init__(self, url_map, *items):
    super(RegexConverter, self).__init__(url_map)
    self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter

@app.route('/files')
@app.route('/files/')
@app.route('/files<regex(".*"):path>')
def files(path=None):
  if path == None:
    path = '/' 

  files = os.listdir(path)

  result = {
      'files': files,
      'path': path
      }

  return jsonify(result)

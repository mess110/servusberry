import os

from servusberry import app
from flask import jsonify

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

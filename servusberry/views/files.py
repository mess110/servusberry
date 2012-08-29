import os

from servusberry import app
from flask import jsonify

@app.route('/files')
@app.route('/files/')
@app.route('/files<regex(".*"):path>')
def files(path=None):
  if path == None:
    path = '/' 

  if not os.path.exists(path):
    return jsonify({'code': 1, 'message': 'file does not exist'})

  files = os.listdir(path)

  result = {
      'files': files,
      'path': path
      }

  return jsonify(result)

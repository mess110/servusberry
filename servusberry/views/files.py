import os

from servusberry import app
from flask import jsonify, request

@app.route('/files')
@app.route('/files/')
@app.route('/files<regex(".*"):path>', methods=['GET', 'POST'])
def files(path=None):
  if path == None:
    path = '/' 

  if not os.path.exists(path):
    return jsonify({'code': 1, 'message': 'file does not exist'})

  files = []
  is_folder = False
  root, ext = os.path.splitext(path)

  if not os.path.isfile(path):
    files = os.listdir(path)
    is_folder = True

  result = {
      'files': files,
      'is-folder': is_folder,
      'path': path,
      'extension': ext
      }

  if request.method == 'POST':
    return jsonify({})
  else:
    return jsonify(result)

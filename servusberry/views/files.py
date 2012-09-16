import os

from flask import jsonify
from flask import request
from servusberry import app
from servusberry.lib.executor import Executor
from servusberry.lib.exceptions import api_exception 

@app.route('/files')
@app.route('/files/')
@app.route('/files<regex(".*"):path>', methods=['GET', 'POST', 'DELETE'])
def files(path=None):
  if path == None:
    path = '/' 

  if not os.path.exists(path):
    return api_exception(1, 'file does not exist')

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

  exe = Executor(result)

  if request.method == 'POST':
    if is_folder == True:
      return api_exception(2, 'can not execute folder')

    if not exe.supported_format():
      return api_exception(3, 'don\'t know what to do with this file')

    return jsonify(exe.do_it())
  elif request.method == 'DELETE':
    if not exe.supported_format():
      return api_exception(4, 'can\'t delete this file format')

    return jsonify(exe.remove())

  return jsonify(result)

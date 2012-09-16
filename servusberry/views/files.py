import os

from flask import jsonify
from flask import request
from servusberry import app
from servusberry.lib.executor import Executor
from servusberry.lib.exceptions import file_does_not_exist 
from servusberry.lib.exceptions import not_executable 
from servusberry.lib.exceptions import unknown_file_type 
from servusberry.lib.exceptions import undeletable 

@app.route('/files')
@app.route('/files/')
@app.route('/files<regex(".*"):path>', methods=['GET', 'POST', 'DELETE'])
def files(path=None):
  if path == None:
    path = '/' 

  if not os.path.exists(path):
    return file_does_not_exist()

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
      return not_executable()

    if not exe.supported_format():
      return unknown_file_type() 

    return jsonify(exe.do_it())
  elif request.method == 'DELETE':
    if not exe.supported_format():
      return undeletable() 

    return jsonify(exe.remove())

  return jsonify(result)

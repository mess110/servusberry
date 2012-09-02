import os

from servusberry import app
from flask import jsonify, request
from servusberry.lib.executor import Executor
from servusberry.lib.exceptions import api_exception 

@app.route('/files')
@app.route('/files/')
@app.route('/files<regex(".*"):path>', methods=['GET', 'POST'])
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

  if request.method == 'POST':
    if is_folder == True:
      return api_exception(1, 'can not execute folder')

    # TODO fix this. its a bad idea to rewrite result variable
    exe = Executor(result)

    if not exe.supported_format():
      return api_exception(1, 'don\'t know what to do with this file')

    result = exe.do_it()

  return jsonify(result)

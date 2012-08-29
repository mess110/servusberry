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

  if request.method == 'GET':
    if is_folder == True:
      return api_exception(1, 'can not execute folder')

    exe = Executor(result)
    result = exe.do_it()

  return jsonify(result)

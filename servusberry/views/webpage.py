from servusberry import app
from flask import jsonify

from servusberry.lib.command_builder import kill_command 
from servusberry.lib.executor import Executor

@app.route('/', methods=['GET'])
def index():
  return jsonify({})

@app.route('/killall', methods=['POST'])
def killall():
  cmd = kill_command('mpg123')
  Executor.execute_cmd(cmd)

  return jsonify({'killed': 'all'})

from servusberry import app
from flask import jsonify

from servusberry.lib.command_builder import kill_cmd, update_cmd
from servusberry.lib.executor import Executor

@app.route('/')
@app.route('/ping')
def index():
  return jsonify({'servusberry': 'server', 'version': 1}) 

@app.route('/killall', methods=['POST'])
def killall():
  cmd = kill_cmd('mpg123')
  Executor.execute_cmd(cmd)

  cmd = kill_cmd('/usr/bin/omxplayer.bin')
  Executor.execute_cmd(cmd)

  return jsonify({'killed': 'all'})

@app.route('/update', methods=['POST'])
def update():
  cmd = update_cmd(app.root_path)
  Executor.execute_cmd(cmd)

  return jsonify({})

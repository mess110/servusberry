from servusberry import app
from flask import jsonify

from servusberry.lib.command_builder import kill_cmd, update_cmd, mute_cmd
from servusberry.lib.executor import Executor

@app.route('/')
@app.route('/ping')
def index():
  stats = Executor.stats()

  return jsonify(stats)

@app.route('/killall', methods=['POST'])
def killall():
  cmd = kill_cmd('mpg123')
  Executor.execute_cmd(cmd)

  cmd = kill_cmd('/usr/bin/omxplayer.bin')
  Executor.execute_cmd(cmd)

  return jsonify({'killed': 'all'})

@app.route('/mute', methods=['GET'])
def mute():
  Executor.execute_cmd(mute_cmd())
  return jsonify({})

@app.route('/update', methods=['POST'])
def update():
  cmd = update_cmd(app.root_path)
  Executor.execute_cmd(cmd)

  return jsonify({})

from flask import jsonify
from servusberry import app

from servusberry.lib.command_builder import kill_cmd
from servusberry.lib.command_builder import update_cmd
from servusberry.lib.executor import Executor

@app.route('/')
@app.route('/ping')
def index():
  stats = Executor.stats()
  return jsonify(stats)

@app.route('/killall', methods=['POST'])
def killall():
  kill_cmd('mpg123')
  kill_cmd('/usr/bin/omxplayer.bin')

  return jsonify({'killed': 'all'})

@app.route('/update', methods=['POST'])
def update():
  update_cmd()
  return jsonify({'updated': True})

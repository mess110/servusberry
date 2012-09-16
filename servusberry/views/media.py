from flask import jsonify
from servusberry import app

from servusberry.lib.command_builder import mute_cmd
from servusberry.lib.command_builder import volume_cmd
from servusberry.lib.command_builder import avi_toggle_play
from servusberry.lib.exceptions import invalid_volume_param
from servusberry.lib.exceptions import missing_volume_param
from servusberry.lib.executor import Executor

@app.route('/mute', methods=['POST'])
def mute():
  Executor.execute_cmd(mute_cmd())
  return jsonify({'volume_change': 'mute'})

@app.route('/volume', methods=['POST'])
@app.route('/volume/', methods=['POST'])
@app.route('/volume/<string:amount>', methods=['POST'])
def volumne(amount=None):
  if amount == None:
    return missing_volume_param()

  if not (amount.endswith('+') or amount.endswith('-')):
    return invalid_volume_param()

  if not amount[:-1].isdigit():
    return invalid_volume_param()

  cmd = volume_cmd(amount)
  Executor.execute_cmd(cmd)

  return jsonify({'volume_change': amount})

@app.route('/play')
def play():
  Executor.execute_cmd(avi_toggle_play())
  return jsonify({'toggle_play': True})
  

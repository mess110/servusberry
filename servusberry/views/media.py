from flask import jsonify
from servusberry import app

from servusberry.lib.command_builder import mute_cmd
from servusberry.lib.command_builder import volume_cmd
from servusberry.lib.command_builder import avi_toggle_play
from servusberry.lib.command_builder import avi_seek
from servusberry.lib.exceptions import invalid_volume_param
from servusberry.lib.exceptions import missing_volume_param
from servusberry.lib.executor import Executor

@app.route('/mute', methods=['POST'])
def mute():
  mute_cmd()
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

  volume_cmd(amount)

  return jsonify({'volume_change': amount})

@app.route('/play')
def play():
  avi_toggle_play()
  return jsonify({'toggle_play': True})

@app.route('/seek/<int:seek>')
def seek(seek=None):
  avi_seek(seek)
  return jsonify({'seek': True})

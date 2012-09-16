from flask import jsonify
from servusberry import app

from servusberry.lib.command_builder import mute_cmd
from servusberry.lib.command_builder import volume_cmd
from servusberry.lib.exceptions import api_exception
from servusberry.lib.executor import Executor

@app.route('/mute', methods=['POST'])
def mute():
  Executor.execute_cmd(mute_cmd())
  return jsonify({'volume_change': 'mute'})

@app.route('/volume/<string:amount>', methods=['POST'])
def volumne(amount=None):
  if amount == None:
    return api_exception(5, 'no volume specified')

  if not (amount.endswith('+') or amount.endswith('-')):
    return api_exception(6, 'invalid volume param. must be a number ending with + or -')

  if not amount[:-1].isdigit():
    return api_exception(7, 'invalid volume param. must be a number ending with + or -')

  cmd = volume_cmd(amount)
  Executor.execute_cmd(cmd)

  return jsonify({'volume_change': amount})

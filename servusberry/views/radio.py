from servusberry import app
from flask import jsonify, request

from servusberry.lib.command_builder import audio_cmd
from servusberry.lib.executor import Executor
from servusberry.lib.exceptions import api_exception

@app.route('/radio', methods=['GET', 'POST'])
@app.route('/radio/', methods=['GET', 'POST'])
def radio():
  radios = {
      'FM - The Chillout Lounge': 'http://64.71.184.99:8010/',
      'JFR Radio': 'http://uk1.internet-radio.com:15074/',
      'Rocky FM': 'http://tuner.rockyfm.de:80/',
      'RockRadio1.Com': 'http://91.121.201.88:8000/'
      }

  if request.method == 'POST':
    name = request.args.get('name')
    url = request.args.get('url')

    if name != None:
      if radios.has_key(name):
        play_station(radios[name])
      else:
        return api_exception(5, 'radio station does not exist')
    elif url != None:
      play_station(url)
    else:
      return api_exception(4, 'name or url param required')

  return jsonify(radios)

def play_station(uri):
  cmd = audio_cmd(uri)
  Executor.execute_cmd(cmd)

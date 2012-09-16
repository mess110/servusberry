from flask import jsonify
from flask import request
from servusberry import app

from servusberry.lib.command_builder import audio_cmd
from servusberry.lib.executor import Executor
from servusberry.lib.exceptions import invalid_radio_params 
from servusberry.lib.exceptions import invalid_radio_station 

@app.route('/radio', methods=['GET', 'POST'])
@app.route('/radio/', methods=['GET', 'POST'])
def radio():
  radios = {
      'FM-TheChilloutLounge': 'http://64.71.184.99:8010/',
      'JFRRadio': 'http://uk1.internet-radio.com:15074/',
      'RockyFM': 'http://tuner.rockyfm.de:80/',
      'RockRadio1.Com': 'http://91.121.201.88:8000/'
      }

  if request.method == 'POST':
    name = request.args.get('name')
    url = request.args.get('url')

    if name != None:
      if radios.has_key(name):
        play_station(radios[name])
      else:
        return invalid_radio_station()
    elif url != None:
      play_station(url)
    else:
      return invalid_radio_params()

  return jsonify(radios)

def play_station(uri):
  cmd = audio_cmd(uri)
  Executor.execute_cmd(cmd)

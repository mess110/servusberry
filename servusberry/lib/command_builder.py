def audio_cmd(path):
  return 'mpg123 ' + path + ' &'

def avi_cmd(path):
  return 'omxplayer -r -o hdmi ' + path + ' &'

def kill_cmd(program):
  return 'killall -9 ' + program + ' &'

def update_cmd(path):
  return 'sh ' + path + '/../update.sh &'

def mute_cmd():
  return 'amixer set PCM toggle'

def volume_cmd(vol):
  return 'amixer set PCM ' + vol

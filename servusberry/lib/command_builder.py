def audio_cmd(path):
  return 'mpg123 ' + path + ' &'

def avi_cmd(path):
  return 'omxplayer -r -o hdmi ' + path + ' &'

def kill_cmd(program):
  return 'killall -9 ' + program + ' &'

def audio_cmd(path):
  return 'mpg123 ' + path + ' &'

def avi_cmd(path):
  fifo = '/tmp/omxplayer_fifo'

  cmd = 'rm -f ' + fifo + ';'
  cmd += 'mkfifo ' + fifo + ';'
  cmd += 'omxplayer -r -o hdmi ' + path +' < ' + fifo + ' &'
  cmd += 'sleep 0.1;'
  cmd += 'echo . > ' + fifo + ' &'

  return cmd

def avi_toggle_play():
  fifo = '/tmp/omxplayer_fifo'

  return 'echo -n p > ' + fifo + ' &'

def kill_cmd(program):
  return 'killall -9 ' + program + ' &'

def update_cmd(path):
  return 'sh ' + path + '/../update.sh &'

def mute_cmd():
  return 'amixer set PCM toggle'

def volume_cmd(vol):
  return 'amixer set PCM ' + vol

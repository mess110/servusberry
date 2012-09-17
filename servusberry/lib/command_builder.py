from sh import killall
from sh import git
from sh import amixer
from sh import mpg123

def audio_cmd(path):
  mpg123(path, _bg=True)

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

def avi_seek(seek):
  fifo = '/tmp/omxplayer_fifo'

  direction = ''
  if seek == 1:
    direction = "$'\x1b\x5b\x42'"
  elif seek == 2:
    direction = "$'\x1b\x5b\x44'"
  elif seek == 3:
    direction = "$'\x1b\x5b\x43'"
  elif seek == 4:
    direction = "$'\x1b\x5b\x41'"
  else:
    direction = "."

  return  'echo -n ' + direction + ' > ' + fifo + ' &'

def kill_cmd(program):
  killall('-9', program, _bg=True)

def update_cmd(path):
  git('pull')

def mute_cmd():
  amixer('set', 'PCM', 'toggle', _bg=True)

def volume_cmd(vol):
  amixer('set', 'PCM', vol, _bg=True)

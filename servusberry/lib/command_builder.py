import sh

def audio_cmd(path):
  sh.mpg123(path, _bg=True)

def avi_cmd(path):
  fifo = '/tmp/omxplayer_fifo'

  sh.rm('-f', fifo)
  sh.mkfifo(fifo)
  sh.omxplayer('-r', '-o', 'hdmi', path, '<', fifo, _bg=True)
  sh.sleep(0.1)
  sh.echo('.', '>', fifo, _bg=True)

def avi_toggle_play():
  fifo = '/tmp/omxplayer_fifo'

  sh.echo('-n', 'p', '>', fifo, _bg=True)

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

  sh.echo('-n', direction, '>', fifo, _bg=True)

def kill_cmd(program):
  sh.killall('-9', program, _bg=True)

def update_cmd():
  sh.git('pull')

def mute_cmd():
  sh.amixer('set', 'PCM', 'toggle', _bg=True)

def volume_cmd(vol):
  sh.amixer('set', 'PCM', vol, _bg=True)

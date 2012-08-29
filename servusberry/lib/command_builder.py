def mp3_command(path):
  return 'mpg123 ' + path + ' &'

def avi_command(path):
  return ''

def kill_command(program):
  return 'killall -9 ' + program + ' &'

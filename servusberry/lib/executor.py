from servusberry.config import version
from servusberry.lib.command_builder import audio_cmd
from servusberry.lib.command_builder import avi_cmd
from servusberry.lib.util import human_time
from servusberry.lib.util import get_uptime
from subprocess import call

class Executor:

  @staticmethod
  def execute_cmd(cmd):
    call(cmd, shell=True)

  @staticmethod
  def stats():
    uptime, idletime = get_uptime() 

    return {
      'servusberry': 'server',
      'version': version(),
      'uptime': uptime,
      'uptime': human_time(uptime),
      'idletime': human_time(idletime),
      'raw': {
        'uptime': uptime,
        'idletime': idletime
      }
    }

  def __init__(self, file_info):
    self.file_info = file_info

  def supported_format(self):
    if self.__is_video():
      return True
    if self.__is_mp3():
      return True

    return False

  def do_it(self):
    file_path = self.file_info['path']

    if self.__is_video():
      cmd = avi_cmd(file_path)
      Executor.execute_cmd(cmd)

      return { 'avi': cmd }
    elif self.__is_mp3():
      cmd = audio_cmd(file_path)
      Executor.execute_cmd(cmd)

      return { 'mp3': 1 }
    else:
      return { 'false': 0 }

  # TODO: implement remove
  def remove(self):
    return { 'removed': False }

  def __is_video(self):
    return self.file_info['extension'] == '.avi'

  def __is_mp3(self):
    return self.file_info['extension'] == '.mp3'

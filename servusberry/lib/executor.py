from servusberry.config import version
from servusberry.lib.command_builder import audio_cmd
from servusberry.lib.command_builder import avi_cmd
from servusberry.lib.util import human_time
from servusberry.lib.util import get_uptime
from subprocess import call

class Executor:

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
    return self.file_info['extension'] in ['.avi', '.mp3']

  def do_it(self):
    file_path = self.file_info['path']

    if self.__is_video():
      avi_cmd(file_path)

      return { 'avi': cmd }
    elif self.__is_mp3():
      audio_cmd(file_path)

      return { 'mp3': 1 }
    else:
      return { 'false': 0 }

  # TODO: implement remove
  def remove(self):
    return { 'removed': False }

  def __is_video(self):
    return self.file_info['extension'] in ['.avi']

  def __is_mp3(self):
    return self.file_info['extension'] in ['.mp3']

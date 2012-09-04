from servusberry.lib.command_builder import audio_cmd, avi_cmd 
from subprocess import call

class Executor:

  @staticmethod
  def execute_cmd(cmd):
    call(cmd, shell=True)

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

  def remove(self):
    return { 'removed': True }

  def __is_video(self):
    return self.file_info['extension'] == '.avi'

  def __is_mp3(self):
    return self.file_info['extension'] == '.mp3'

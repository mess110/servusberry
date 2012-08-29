from servusberry.lib.command_builder import mp3_cmd, avi_cmd 
from subprocess import call

class Executor:

  @staticmethod
  def execute_cmd(cmd):
    call(cmd, shell=True)

  def __init__(self, file_info):
    self.file_info = file_info

  def do_it(self):
    file_path = self.file_info['path']

    if self.__is_video():
      cmd = avi_cmd(file_path)
      Executor.execute_cmd(cmd)

      return { 'avi': cmd }
    elif self.__is_mp3():
      cmd = mp3_cmd(file_path)
      Executor.execute_cmd(cmd)

      return { 'mp3': 1 }
    else:
      return { 'false': 0 }

  def __is_video(self):
    return self.file_info['extension'] == '.avi'

  def __is_mp3(self):
    return self.file_info['extension'] == '.mp3'

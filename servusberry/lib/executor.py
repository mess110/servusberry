from subprocess import call

class Executor:
  def __init__(self, file_info):
    self.file_info = file_info

  # TODO create a command builder
  def do_it(self):
    file_path = self.file_info['path']

    if self.__is_video():
      cmd = 'totem ' + file_path
      self.__execute_cmd(cmd)

      return { 'avi': cmd }
    elif self.__is_mp3():
      cmd = 'mpg123 ' + file_path
      self.__execute_cmd(cmd)

      return { 'mp3': 1 }
    else:
      return { 'false': 0 }

  def __is_video(self):
    return self.file_info['extension'] == '.avi'

  def __is_mp3(self):
    return self.file_info['extension'] == '.mp3'

  def __execute_cmd(self, cmd):
    cmd = cmd + ' &'
    call(cmd, shell=True)

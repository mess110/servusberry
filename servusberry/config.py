from os import path
from werkzeug.routing import BaseConverter

def config(app):
  add_converters(app)

  config_path = path.join(app.instance_path, 'app.cfg')
  try:
    app.config.from_pyfile(config_path)
  except IOError:
    raise SystemExit("\nMissing config: %s\n" % config_path)

def version():
  return '1.0.0'

def add_converters(app):
  app.url_map.converters['regex'] = RegexConverter


class RegexConverter(BaseConverter):
  def __init__(self, url_map, *items):
    super(RegexConverter, self).__init__(url_map)
    self.regex = items[0]

from os import path

def config(app):
  config_path = path.join(app.instance_path, 'app.cfg')
  try:
    app.config.from_pyfile(config_path)
  except IOError:
    raise SystemExit("\nMissing config: %s\n" % config_path)

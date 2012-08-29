import os
from servusberry import app

if __name__ == '__main__':
  host = app.config['HOST']
  port = int(app.config['PORT'])
  debug = app.config['DEBUG']

  app.run(host=host, port=port, debug=debug)

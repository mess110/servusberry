from servusberry import app
from flask import jsonify
from servusberry.lib.transmission_remote import list_torrents

@app.route('/torrents', methods=['GET'])
def torrents():
  result = list_torrents()
  return jsonify({'torrents': result })

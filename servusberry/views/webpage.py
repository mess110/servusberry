from servusberry import app
from flask import jsonify

@app.route('/', methods=['GET'])
def index():
  return jsonify({})

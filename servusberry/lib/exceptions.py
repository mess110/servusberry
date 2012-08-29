from flask import jsonify

def api_exception(code, message):
  return jsonify({
    'code': code,
    'message': message
    })

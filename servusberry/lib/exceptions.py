from flask import jsonify

def api_exception(code, message):
  return jsonify({
    'code': code,
    'message': message })

def file_does_not_exist():
  return api_exception(1, 'file does not exist')

def not_executable():
  return api_exception(2, 'can not execute folder')

def unknown_file_type():
  return api_exception(3, 'unkown file type')

def undeletable():
  return api_exception(4, 'can\'t delete this file format')

def missing_volume_param():
  return api_exception(5, 'no volume specified')

def invalid_volume_param():
  return api_exception(6, 'invalid volume param. must be a number ending with + or -')

def invalid_radio_params():
  return api_exception(7, 'name or url param required')

def invalid_radio_station():
  return api_exception(8, 'radio station doesn\'t exist')

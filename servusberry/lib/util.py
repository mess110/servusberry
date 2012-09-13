import datetime

def get_uptime():
  return [round(float(field)) for field in open("/proc/uptime").read().split()]

def human_time(t):
  return str(datetime.timedelta(seconds=t))

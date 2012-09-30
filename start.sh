killall -9 transmission-deamon
transmission-daemon --no-blocklist --no-auth --allowed="192.168.*.*, 127.0.0.1"

python `pwd`/app.py &

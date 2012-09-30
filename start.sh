SCRIPT_PATH=`readlink -f $0`
SCRIPT_DIR=`dirname $SCRIPT_PATH`

sudo killall -9 /usr/bin/transmission-daemon
killall -9 transmission-daemon
transmission-daemon --no-blocklist --no-auth --allowed="192.168.*.*, 127.0.0.1"

python $SCRIPT_DIR/app.py &

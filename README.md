# mounting external harddrive
sudo blkid

sudo mkdir -p /media/ExternalHd
sudo chmod 755 /media/ExternalHd

sudo vim /etc/fstab

UUID=4956-13EB  /media/ExternalHd   vfat defaults,user,exec,umask=000 0 0

or

/dev/sda1 /media/ExternalHd vfat defaults,user,exec,umask=000 0 0

# starting tranmission-daemon


For wav you can use aplay. For mp3 you can use mpg123

omxplayer -r -o hdmi Doctor\ Who\ -\ 3x11\ -\ Utopia.avi

mkfifo /tmp/cmd

omxplayer -ohdmi mymedia.avi < /tmp/cmd

echo . > /tmp/cmd (Start omxplayer running as the command will initial wait for input via the fifo)

echo -n p > /tmp/cmd - Playback is paused

echo -n q > /tmp/cmd - Playback quits

implement autoupdate


# AUDIO
amixer set PCM toggle
amixer set PCM 1000+
amixer set PCM 1000-

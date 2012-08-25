# mounting external harddrive
sudo blkid

sudo mkdir -p /media/ExternalHd
sudo chmod 755 /media/ExternalHd

sudo vim /etc/fstab

UUID=4956-13EB  /media/ExternalHd   vfat defaults,user,exec,umask=000 0 0

or

/dev/sda1 /media/ExternalHd vfat defaults,user,exec,umask=000 0 0

# starting tranmission-daemon

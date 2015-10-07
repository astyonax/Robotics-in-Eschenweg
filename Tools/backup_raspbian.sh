DEVICE=/dev/mmcblk0
PARTITIONS=/dev/mmcblk0p*
echo $PARTITIONS

sudo umount ${PARTITIONS}
sudo dd bs=4M if=${DEVICE} | pv | dd of='raspbian_'`date +%d.%m.%y`'.img' conv=notrunc

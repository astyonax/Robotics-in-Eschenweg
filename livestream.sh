# from http://pi.gbaman.info/?p=150

# this has to be run in the PI
PI_IP_ADDRESS=`ifconfig wlan0| awk '/inet addr/{print substr($2,6)}'`

gst-launch-1.0 -v tcpclientsrc host=${PI_IP_ADDRESS} port=5000  ! gdpdepay !  rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false

# run the following in the receiver
echo "RUN THIS ON YOUR PC:
gst-launch-1.0 -v tcpclientsrc host=${PI_IP_ADDRESS} port=5000  ! gdpdepay !  rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=false "



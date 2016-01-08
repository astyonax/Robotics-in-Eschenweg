`mencoder tv://  -tv driver=v4l2:width=320:height=240:fps=24:device=/dev/video0  -ovc xvid -xvidencopts turbo:nochroma_me:notrellis:max_bframes=0:vhq=0:bitrate=2000 -nosound  -of avi -o - |netcat -u 192.168.42.10 3000`


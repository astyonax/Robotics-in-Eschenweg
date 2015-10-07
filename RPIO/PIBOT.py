import RPi.GPIO as GPIO
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT) 
GPIO.setup(15,GPIO.OUT)

do=GPIO.output

def keydown(key):
	if key == simplegui.KEY_MAP['up']:
  		forw(1);
	elif key == simplegui.KEY_MAP['down']:
  		back(1);
	elif key == simplegui.KEY_MAP['left']:
		left(1);
	elif key == simplegui.KEY_MAP['right']:
  		right(1);

def reset():
	for pin in [7,11,13,15]:
		do(pin,0)	

def forw(t):
	GPIO.output(7,True);
	GPIO.output(13,True);

	time.sleep(t);

	GPIO.output(7,False);
	GPIO.output(13,False);

def back(t):
	GPIO.output(11,True);
	GPIO.output(15,True);

	time.sleep(t);

	GPIO.output(11,False);
	GPIO.output(15,False);

def left(t):
	GPIO.output(13,True);

	time.sleep(t);

	GPIO.output(13,False);

def left_fast(t):
	GPIO.output(13,True);
	GPIO.output(11,True);

	time.sleep(t);

	GPIO.output(13,False);
	GPIO.output(11,False);

def right(t):
	GPIO.output(7,True);

	time.sleep(t);

	GPIO.output(7,False);

def right_fast(t):
	GPIO.output(7,True);
	GPIO.output(15,True);

	time.sleep(t);

	GPIO.output(7,False);
	GPIO.output(15,False);

def GOGO():
	f = simplegui.create_frame('ROBOT',100,100)
	f.set_keydown_handler(keydown)
	f.start()

if __name__=='__main__':
	GOGO()

import RPi.GPIO as GPIO
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import time

GPIO.setmode(GPIO.BOARD)

RF=7
RB=11
LF=15
LB=13
PWMR=37
PWML=40


PINS=[RF,RB,LF,LB,PWMR,PWML]
for j in PINS:
	GPIO.setup(j,GPIO.OUT)

enR = GPIO.PWM(PWMR, 50) 
enL = GPIO.PWM(PWML, 50)

enR.start(100)
enL.start(100)

def reset():
	for pin in PINS:
		do(pin,0)	

def ON():
	GPIO.output(RF,True);
	GPIO.output(LF,True);

def OFF():
	GPIO.output(RF,False);
	GPIO.output(LF,False);


def testme():
	ON()
	time.sleep(2)
	OFF()

	exit(1)

try:
	ON()	
	for dc in xrange(0,100,10):
		enR.stop()
		enL.stop()
		enL.start(dc)
		enR.start(dc)
		print dc
		time.sleep(2)
	OFF()
except:
	enR.stop()
	enL.stop()
	reset()
	GPIO.cleanup()


'''
def keydown(key):
	if key == simplegui.KEY_MAP['up']:
  		forw(1);
	elif key == simplegui.KEY_MAP['down']:
  		back(1);
	elif key == simplegui.KEY_MAP['left']:
		left(1);
	elif key == simplegui.KEY_MAP['right']:
  		right(1);
	elif key == simplegui.KEY_MAP['space']:
		reset()


def back(t):
	reset()
	GPIO.output(11,True);
	GPIO.output(15,True);

def left(t):
	reset()
	GPIO.output(13,True);

def left_fast(t):
	reset()
	GPIO.output(13,True);
	GPIO.output(11,True);


def right(t):
	reset()
	GPIO.output(7,True);


def right_fast(t):
	reset()
	GPIO.output(7,True);
	GPIO.output(15,True);


def GOGO():
	f = simplegui.create_frame('ROBOT',100,100)
	f.set_keydown_handler(keydown)
	f.start()

if __name__=='__main__':
	GOGO()
'''

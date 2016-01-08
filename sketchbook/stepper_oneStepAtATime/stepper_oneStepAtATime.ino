
/* 
 Stepper Motor Control - one step at a time
 
 This program drives a unipolar or bipolar stepper motor. 
 The motor is attached to digital pins 8 - 11 of the Arduino.
 
 The motor will step one step at a time, very slowly.  You can use this to
 test that you've got the four wires of your stepper wired to the correct
 pins. If wired correctly, all steps should be in the same direction.
 
 Use this also to count the number of steps per revolution of your motor,
 if you don't know it.  Then plug that number into the oneRevolution
 example to see if you got it right.
 
 Created 30 Nov. 2009
 by Tom Igoe
 
 */

#include <Stepper.h>
const float stride_angle = 5.625;
const int rpm = 30;
const int stepsPerRevolution = 360/stride_angle;  // change this to fit the number of steps per revolution
                                     // for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepperCW(stepsPerRevolution, 2,3,4,5);            
Stepper myStepperCCW(stepsPerRevolution, 2,5,4,3);            

void CW(float n){
  myStepperCW.setSpeed(rpm);
  myStepperCW.step(n*stepsPerRevolution);
}
void CCW(float n){
  myStepperCCW.setSpeed(rpm);
  myStepperCCW.step(n*stepsPerRevolution);
}
void ruota(float angle, float n){
  if (angle > 180){
    CCW(n);
  }
  else
  {
    CW(n);
  }
}


void setup() {
  // initialize the serial port:
  Serial.begin(9600);
}


float angle=0;
float n=.5;
float dangle=stride_angle*n;

void loop() {
  // step one step:
  
  ruota(angle,.5);
  delay(500);
  angle+=dangle;
  angle=fmod(angle,360);
  Serial.println(angle);
  

}


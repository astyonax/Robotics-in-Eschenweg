
#define P2(A) (A)*(A)
//HC RS04 Sensore ultrasuoni
int triggerPort = 7;
int echoPort = 8;
 
void setup() {
pinMode (3, OUTPUT); 
pinMode( triggerPort, OUTPUT );
pinMode( echoPort, INPUT );
Serial.begin( 9600 );
Serial.println( "Sensore ultrasuoni: ");
 
}
float alpha=.01;
float distance_old=.1;
void loop() {
//porta bassa l'uscita del trigger
digitalWrite( triggerPort, LOW );
 
//invia un impulso di 10microsec su trigger
digitalWrite( triggerPort, HIGH );
delayMicroseconds( 10 );
digitalWrite( triggerPort, LOW );
 
float duration = pulseIn( echoPort, HIGH );
// distanza in cm
float distance = (duration/2) / 29.1;

float dmax=200.;
distance= distance/dmax;
if (distance >distance_old*5){distance=distance_old;}
distance=distance*alpha+(distance_old)*(1-alpha);
distance_old=distance;
if( distance > 1 || distance <0) {
;
}
else { 
  analogWrite(3,255*distance);
//  delay();
//  for (int j=0;j<100;j++){
//    analogWrite(4,255);
//    delay(200*distance);
//    analogWrite(4,255*distance);
//    delay(200*distance);
//  }
}
 
//aspetta 1.5 secondi

}

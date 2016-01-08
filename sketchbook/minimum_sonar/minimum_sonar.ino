
//HC RS04 Sensore ultrasuoni
int triggerPort = 13;
int echoPort = 12;
 
void setup() {
pinMode( triggerPort, OUTPUT );
pinMode( echoPort, INPUT );
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
}

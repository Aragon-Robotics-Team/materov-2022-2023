int ControlPin1 = 9; // 
int ControlPin2= 10; // 
int Sec = 0; //Should be =1000 for actual dleays to happen
int setSec = 9*Sec; //90 seconds to put Float at its place
int sinkSec = 3*Sec; //30 seconds to sink
int floatSec = sinkSec; //for now sinking time and floating time

void setup(){
Serial.begin(9600);
pinMode(ControlPin1, OUTPUT);
pinMode(ControlPin2, OUTPUT);
}

void loop(){
    floatyFloat(); // protract/pull actuator to get water into the 
    delay(sinkSec*50); //time for ROV to sink to bottom of pool
    //note: this goes on indefinitely so make sure to unplug battery when the actuator reaches where it needs to go
  } //will keep repeating this until it is picked back up by ROV or MATE scuba diver person

void sinkFloat() { // push out water/retract Actuator
digitalWrite(ControlPin2, LOW);
digitalWrite(ControlPin1, HIGH);
delay(3000); // max range is 30000, mid point is 15000
}

void floatyFloat() { // pull in water/retract Actuator
digitalWrite(ControlPin2, HIGH);
digitalWrite(ControlPin1, LOW);
delay(3000); // max range is 30000, mid point is 15000
}

void InitialPosition(){
digitalWrite(ControlPin2, HIGH);
digitalWrite(ControlPin1, LOW);
delay(30000);
}

void stopActuator(){
digitalWrite(ControlPin2, LOW);
digitalWrite(ControlPin1, LOW);
delay(7000);
}

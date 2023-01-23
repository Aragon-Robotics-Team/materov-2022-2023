int ControlPin1 = 9; // 
int ControlPin2= 10; // 
int Sec = 1000;
int setSec = 90*Sec; //90 seconds to put Float at its place
int sinkSec = 30*Sec; //30 seconds to sink
int floatSec = sinkSec; //for now sinking time and floating time

void setup(){
Serial.begin(9600);
pinMode(ControlPin1, OUTPUT);
pinMode(ControlPin2, OUTPUT);
}

void loop(){
    delay(setSec); //time for ROV to put float in its place
    sinkFloat(); 
    delay(sinkSec); //time for ROV to sink to bottom of pool
    floatyFloat();
    delay(floatSec); //time for ROV to float to top of pool
    sinkFloat();
    delay(sinkSec); //time for ROV to sink to bottom 2nd time
    floatyFloat();
  } //will keep repeating this until it is picked back up by ROV or MATE scuba diver person

void sinkFloat() { // pull in water/retract Actuator
digitalWrite(ControlPin2, LOW);
digitalWrite(ControlPin1, HIGH);
delay(15000); // max range is 30000, mid point is 15000
}

void floatyFloat() { // pull in water/retract Actuator
digitalWrite(ControlPin2, HIGH);
digitalWrite(ControlPin1, LOW);
delay(15000); // max range is 30000, mid point is 15000
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


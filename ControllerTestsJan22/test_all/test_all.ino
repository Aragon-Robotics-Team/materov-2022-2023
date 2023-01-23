#include <Servo.h>

Servo thruster1;
Servo thruster2;
Servo thruster3;
Servo thruster4;
Servo thruster5;
Servo thruster6;
Servo thrusters[] = {thruster1, thruster2, thruster3, thruster4, thruster5, thruster6};

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  for(int i = 0; i<6; i++){
    thrusters[i].attach(i+8);
  }
  
  delay(1000);
}

void loop() {

  // put your main code here, to run repeatedly:

  //Running each thruster one at a time for 3 seconds, with 4 second pauses

  for (int i = 0; i<6; i++){
    int pinNumber = i+8;
    Serial.println("This thruster is attached to" + String(pinNumber));
    thrusters[i].writeMicroseconds(1700);
    delay(3000);
    thrusters[i].writeMicroseconds(1500);
    delay(4000);
  }

}

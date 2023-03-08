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

  while(!Serial.available());
  int thrusterToRun = Serial.readStringUntil('\n').toInt() - 8;
  thrusters[thrusterToRun].writeMicroseconds(1800);
  Serial.println("running thruster on pin " + String(thrusterToRun + 8));
  delay(4000);
  thrusters[thrusterToRun].writeMicroseconds(1500);
  Serial.println("done running");
  delay(1000);

  //Documentation: (LF, LB, RF, RB, VL, VR)
  /*
   * 8: 
   * 9: 
   * 10: 
   * 11: 
   * 12: 
   * 13: 
   */

}

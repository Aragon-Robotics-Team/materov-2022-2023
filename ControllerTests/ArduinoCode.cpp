/*

#include <Servo.h>

Servo v1; //Vertical servo
Servo v2; //Other Vertical servo
Servo fr; //front right
Servo fl; // front left
Servo bf; // back right
Servo bl; //back left

Servo myServos[] = {v1, v2, fr, fl, br, bl };


String thrusterSpeed;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(2000);

  v1.attach(2);  //Attaching thruster's to PWM pins on Arduino
  v2.attach(3);
  fr.attach(4);
  fl.attach(5);
  br.attach(6); //check 6 and 7 pins(if they are pwm)
  bl.attach(7);git 
}

void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial.available());

  for(int i=0; i<4; i++){ //replace x with vals
    thrusterSpeed = Serial.readStringUntil(','); //gets the int from the encoded string
    myServos[i].writeMicroseconds(thrusterSpeed.toInt()); //writes the thruster with the value it should have
    thrusterSpeed = ""; //clears the variable
  }
}

*/

//current arduino code

/*

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (!Serial.available());

  String value1 = Serial.readStringUntil(',');
  String value2 = Serial.readStringUntil(',');
  String value3 = Serial.readStringUntil(',');
  String value4 = Serial.readStringUntil(',');
  String value5 = Serial.readStringUntil(',');
  String value6 = Serial.readStringUntil(',');
  Serial.println(value1 + ", " + value2 + ", " 
  + value3 + ", " + value4 + ", " + value5 + ", " + value6);
}

*/
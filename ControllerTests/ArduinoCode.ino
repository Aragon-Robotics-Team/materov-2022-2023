#include <Servo.h>

//global variables for thruster pwms
int br;
int fl;
int bl;
int fr;
int v1;
int v2;

Servo LF_T; //left front
Servo LB_T; //left back
Servo RF_T; //right front
Servo RB_T; //right back
Servo L_VERT; //left vertical
Servo R_VERT; //left vertical



void setup() {
Serial.begin(9600); // set the baud rate
delay(2000);
Serial.println("Arduino is ready!");

//Attaching thrusteeee to PWM pins on arduino
  LF_T.attach(8); 
  LB_T.attach(9);
  RF_T.attach(10);
  RB_T.attach(11);
  L_VERT.attach(12); //check 6 and 7 pins(if they are pwm)
  R_VERT.attach(13);
  
}



void loop() {
  //getting PWM values from computer
  fr = Serial.readStringUntil(',').toInt();
  fl = Serial.readStringUntil(',').toInt();
  br = Serial.readStringUntil(',').toInt();
  bl = ((Serial.readStringUntil(',').toInt() - 1500) * (-1)) + 1500;;
  v1 = Serial.readStringUntil(',').toInt();
  v2 = Serial.readStringUntil(',').toInt();
  // - 1500) * (-1)) + 1500;
  //send pwm values to thrusters
  LF_T.writeMicroseconds(fl);
  LB_T.writeMicroseconds(bl);
  RF_T.writeMicroseconds(fr);
  RB_T.writeMicroseconds(br);
  L_VERT.writeMicroseconds(v1);
  R_VERT.writeMicroseconds(v2);
  
  Serial.println(String(br) + ", " + String(fl) + ", " + String(bl) + ", " + String(fr) + ", " + String(v1) + ", " + String(v2));
  
  delay(50);
  
}
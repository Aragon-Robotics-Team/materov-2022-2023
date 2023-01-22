#include <Servo.h>

//global variables for thruster pwms
int lf;
int lb;
int rf;
int rb;
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

//lf lb rf rb vl vr

void loop() {
  //getting PWM values from computer
  lf = Serial.readStringUntil(',').toInt();
  lb = Serial.readStringUntil(',').toInt();
  rf = Serial.readStringUntil(',').toInt();
  rb = Serial.readStringUntil(',').toInt();
  v1 = Serial.readStringUntil(',').toInt();
  v2 = Serial.readStringUntil(',').toInt();

  //send pwm values to thrusters
  LF_T.writeMicroseconds(lf);
  LB_T.writeMicroseconds(lb);
  RF_T.writeMicroseconds(rf);
  RB_T.writeMicroseconds(rb);
  L_VERT.writeMicroseconds(v1);
  R_VERT.writeMicroseconds(v2);

  Serial.println(
  String(lf) + ", " + String(lb) + ", "
  + String(rf) + ", " + String(rb) + ", "
  + String(v1) + ", " + String(v2)
  );

  delay(50);

}

#include <Servo.h>

//global variables for thruster pwms
int lf;
int lb;
int rf;
int rb;
int v1;
int v2;
int pwmVals[] = {lf, lb, rf, rb, v1, v2};

Servo LF_T; //left front
Servo LB_T; //left back
Servo RF_T; //right front
Servo RB_T; //right back
Servo L_VERT; //left vertical
Servo R_VERT; //left vertical
Servo thrusters[] = {LF_T, LB_T, RF_T, RB_T, L_VERT, R_VERT};

void setup() {
Serial.begin(9600); // set the baud rate
delay(300);

//Attaching thrusters to PWM pins on arduino
for(int i = 0; i<6; i++){
  thrusters[i].attach(i+8);
  }
}

//lf lb rf rb vl vr

void loop() {
  //getting PWM values from computer
  while(!Serial.available());
  
  for(int i = 0; i<5; i++){
    pwmVals[i] = Serial.readStringUntil(',').toInt();
  }
  pwmVals[5] = Serial.readStringUntil('.').toInt();

  //send pwm values to thrusters

  for(int i = 0; i<6; i++){
    thrusters[i].writeMicroseconds(pwmVals[i]);
  }

  Serial.println(String(lf) + ", " + String(lb) + ", " + String(rf) + ", " + String(rb) + ", " + String(v1) + ", " + String(v2));

  delay(50);

}

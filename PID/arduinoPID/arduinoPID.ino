#include <Wire.h>
#include <Servo.h>
#include "MS5837.h"

//PID multipliers
double proportionalGain;
double integralGain;
double derivativeGain;

//used for PID calculations
double error;
double derivativeError;
double previousError;
double integralSum;
double pidOutput;

double proportion_value;
double integral_value;
double derivative_value;

double depth;
double goal = 0.2; // in meters

MS5837 sensor;
int v1;
int v2;
Servo L_VERT;
Servo R_VERT;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin();

  L_VERT.attach(12);
  R_VERT.attach(13);

  sensor.setModel(MS5837::MS5837_02BA);
  sensor.init();
  sensor.setFluidDensity(997); // kg/m^3 (997 freshwater, 1029 for seawater)
  
  tunePID(500,5,10);
  
  delay(2000);
}


  
void loop() {
  // put your main code here, to run repeatedly:
    sensor.read();

    Serial.print("Depth: "); 
    Serial.print(sensor.depth()); 
    Serial.println(" m");
  
    delay(10);
    double sens_depth = (double)sensor.depth(); //casting to double 
    double PWM_Value = PID(sens_depth, 0.2);
    PWM_Value += 1500;
    

    L_VERT.writeMicroseconds(PWM_Value);
    R_VERT.writeMicroseconds(PWM_Value);
    Serial.println(PWM_Value);
    delay(100);
}



//Pid calculations :)
double PID(float depth, double goal) {
  
  error = goal - depth; //depth from sensor
  integralSum += error;
  derivativeError = error - previousError;
  
  proportion_value = proportionalGain * error;
  //integral_value = integralGain * integralSum;
  //derivative_value = derivativeGain * derivativeError;

  pidOutput = proportion_value + integral_value + derivative_value;
  pidOutput = pidOutput;

  pidOutput = max(-400, pidOutput);
  pidOutput = min(400, pidOutput);
  
  previousError = error; //for derivative
  
  return pidOutput;
}




void tunePID(double proportional, double integral, double derivative) {
  proportionalGain = proportional;
  integralGain = integral;
  derivativeGain = derivative;
}
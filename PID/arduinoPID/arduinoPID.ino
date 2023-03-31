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

double bot_width = 17;
double bot_length = 17;

MS5837 sensor;
const int MPU_addr1 = 0x68;
float xAccel, yAccel, zAccel, roll, pitch;

int v1;
int v2;
Servo L_VERT;
Servo R_VERT;

void setup() {
  
  Serial.begin(9600);
  Wire.begin();
  Wire.beginTransmission(MPU_addr1); //begin, send the slave adress (in this case 68)
  Wire.write(0x6B); //make the reset (place a 0 into the 6B register)
  Wire.write(0);
  Wire.endTransmission(true);

  L_VERT.attach(12);
  R_VERT.attach(13);

  sensor.setModel(MS5837::MS5837_02BA);
  sensor.init();
  sensor.setFluidDensity(997); // kg/m^3 (997 freshwater, 1029 for seawater)
  
  tunePID(500,5,10);
  
  delay(2000);
}


  
void loop() {
    // gyro/accel 
    Wire.beginTransmission(MPU_addr1);
    Wire.write(0x3B);  //send starting register address, accelerometer high byte
    Wire.endTransmission(false); //restart for read
    Wire.requestFrom(MPU_addr1, 6, true); //get six bytes accelerometer data
    int t = Wire.read();
    xAccel = (t << 8) | Wire.read();
    t = Wire.read();
    yAccel = (t << 8) | Wire.read();
    t = Wire.read();
    zAccel = (t << 8) | Wire.read();
  
    // IN RADIANS
    roll = atan2(yAccel , zAccel);
    pitch = atan2(-xAccel , sqrt(yAccel * yAccel + zAccel * zAccel)); //account for roll already applied
  
    // TO DEGREES
    // roll *= 180.0 / PI;
    // pitch *= 180.0 / PI;

    
    double depth_diff = bot_width / (tan(roll - PI/2)); // in inches
    double depth_diff /= 39.37; // conversion to meters
    Serial.println(depth_diff);
    Serial.print("roll = ");
    Serial.print(roll);
    Serial.print(", pitch = ");
    Serial.println(pitch);

    // pressure sensor 
    sensor.read();

    Serial.print("Depth: "); 
    Serial.print(sensor.depth()); 
    Serial.println(" m");
  
    double sens_depth = (double)sensor.depth(); //casting to double 
    double L_VERT_PWM = PID(sens_depth + depth_diff, goal);
    double R_VERT_PWM = PID(sens_depth, goal)
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
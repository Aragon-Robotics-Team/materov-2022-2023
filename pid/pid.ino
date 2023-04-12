#include <Wire.h>
#include <Servo.h>
#include "MS5837.h"
#define TCAADDR 0x70

MS5837 depthSensor;
const int MPU_addr1 = 0x68;
float xAccel, yAccel, zAccel, roll, pitch;

double proportionalGain, integralGain, derivativeGain;
double error, derivativeError, previousError, integralSum, pidOutput;
double proportion_value, integral_value, derivative_value;
double depth, goal, depth_diff; // in meters
double bot_width = 17; //in inches

int FRONT_PWM;
int BACK_PWM;
Servo F_VERT;
Servo B_VERT;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  initDepthSensor(0);
  initMPU(1);
}


void loop() {
  getDepth(0);
  getAngle(1);

  Serial.print("Depth: ");
  Serial.print(depth);
  
  Serial.print(" | Roll: ");
  Serial.print(roll);
  
  Serial.print(" | Pitch: ");
  Serial.println(pitch);

  depth_diff = bot_width / (tan(roll - PI/2)); // in inches
  depth_diff /= 39.37; // conversion to meters

  goal = 1.0;

  FRONT_PWM = PID(depth + depth_diff, goal) + 1500;
  BACK_PWM = PID(depth, goal) + 1500;
  
  delay(50);
}





// change SDA/SCL on mux
void selectChannel(int channel) {
  if (channel > 7) return;
 
  Wire.beginTransmission(0x70); // TCA9548A address
  Wire.write(1 << channel);     // send byte to select bus
  Wire.endTransmission();
}


// intialize pressure sensor with necessary delays
void initDepthSensor(int channel) {
  delay(500);
  
  Serial.println("Intializing Depth Sensor...");
  selectChannel(channel);

  while (!depthSensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");
    Serial.println("Blue Robotics Bar30: White=SDA, Green=SCL");
    Serial.println("\n\n\n");
    delay(5000);
  }

  depthSensor.setModel(MS5837::MS5837_02BA);
  depthSensor.setFluidDensity(997);
  depthSensor.init();

  Serial.println("Success!\n");

  delay(500);
}


// intialize MPU6050 with necessary delays
void initMPU(int channel) {
  delay(500);
  Serial.println("Intializing MPU6050...");
  
  selectChannel(channel);
  Wire.beginTransmission(MPU_addr1);                 //begin, send the slave adress (in this case 68)
  Wire.write(0x6B);                                  //make the reset (place a 0 into the 6B register)
  Wire.write(0);
  Wire.endTransmission(true);                        //end the transmission

  Serial.println("Success!\n");
  delay(500);
}


// reads depth from pressure sensor
void getDepth(int channel) {
  selectChannel(channel);
  depthSensor.read();
  depth = (double) depthSensor.depth();  // float -> double
}


// MPU6050 calculations to obtain roll and pitch
void getAngle(int channel) {
  selectChannel(channel);
  
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

  // convert to degrees
  // roll *= 180.0 / PI;
  // pitch *= 180.0 / PI;

  //double depth_diff = 15.5 / (tan(roll - PI/2));
  
}


//Pid calculations :)
double PID(double depth, double goal) {
  
  error = goal - depth; //depth from sensor
  integralSum += error;
  derivativeError = error - previousError;
  
  proportion_value = proportionalGain * error;
  //integral_value = integralGain * integralSum;
  //derivative_value = derivativeGain * derivativeError;

  pidOutput = proportion_value + integral_value + derivative_value;
  pidOutput = -pidOutput;

  pidOutput = max(-400, pidOutput);
  pidOutput = min(400, pidOutput);
  
  previousError = error; //for derivative
  
  return pidOutput;
}


//change gain values
void tunePID(double proportional, double integral, double derivative) {
  proportionalGain = proportional;
  integralGain = integral;
  derivativeGain = derivative;
}
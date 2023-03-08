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

double depth;
double goal;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
}


  
void loop() {
  // put your main code here, to run repeatedly:

  tunePID(1,1,1);
  PID(depth, goal);

}

//Pid calculations :)
double PID(double depth, double goal) {
  
  error = goal - depth; //depth from sensor
  integralSum += error;
  derivativeError = error - previousError;

  pidOutput = (proportionalGain * error) + 
              (integralGain * integralSum) + 
              (derivativeGain * derivativeError); //derivative not divided by time elapsed per loop because it is the same time (plus it wouldn't do much, think of the time as an extra multiplier)

  previousError = error; //for derivative
  
  return pidOutput;
}

void tunePID(double proportional, double integral, double derivative) {
  proportionalGain = proportional;
  integralGain = integral;
  derivativeGain = derivative;
}

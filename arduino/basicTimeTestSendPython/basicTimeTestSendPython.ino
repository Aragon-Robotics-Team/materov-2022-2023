unsigned long myTime = 0;
int givenHour;
int givenMin;
int givenSec;
int storeMin = 0;
int hour = 0;
int min = 0;
int sec = 0;
int store = 0;
int count = 0;
int interval = 0;
int countToMin = 0;
void setup() {
  Serial.begin(9600);
  Serial.print("start");  
}
//min --> 3,600,000
void loop() {
  if(Serial.available() > 0){
  Serial.print("hi");
  givenHour = Serial.readStringUntil(',').toInt();
  givenMin = Serial.readStringUntil(',').toInt();
  givenSec = Serial.readStringUntil(',').toInt();
  Serial.println(givenHour);
  Serial.println(givenMin);
  Serial.println(givenSec);
  }
}

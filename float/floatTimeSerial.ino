unsigned long myTime = 0;
int givenHour;
int givenMin;
int givenSec;
int storeMin = 0;
int hour = 0;
int mins = 0;
int sec = 0;
int store = 0;
int count = 0;
int interval = 0;
int countToMin = 0;

void setup() {
  Serial.begin(9600);
  Serial.print("start");
  Serial.flush();
  while (!Serial.available());
  givenHour = Serial.readStringUntil(',').toInt();
  givenMin = Serial.readStringUntil(',').toInt();
  givenSec = Serial.readStringUntil('.').toInt();
  Serial.println(String(givenHour) + " : " + String(givenMin) + " : " + String(givenSec));

}

//min --> 3,600,000
void loop() {


   // Serial.println(givenHour);
   // Serial.println(givenMin);
   // Serial.println(givenSec);

  myTime = millis();
  sec = givenSec + (myTime/1000);
  if (sec < 60){
    Serial.println(String(givenHour) + " : " + String(givenMin) + " : " + String(sec));
  }
  if (sec >= 60){
    store = (sec % 60);
     if (sec % 60 == 0){
       count = count + 1;
       if(count%52 == 0 || count > 52){
        countToMin = count/52;
        mins = givenMin + countToMin;
        hour = givenHour;
        if(mins%60 ==0){
          mins = 0;
          hour = givenHour + countToMin;
        }
        if(mins > 60){
          mins = mins%60;
        }
       }
     }
    Serial.println(String(hour) + " : " + String(mins) + " : " + String(store));
  }
}
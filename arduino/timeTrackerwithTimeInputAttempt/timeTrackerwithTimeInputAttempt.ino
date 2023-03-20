unsigned long myTime = 0;
int givenHour = 9;
int givenMin = 42;
int givenSec = 50;
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
        min = givenMin + countToMin;
        hour = givenHour;
        if(min%60 ==0){
          min = 0;
          hour = givenHour + countToMin;
        }
        if(min > 60){
          min = min%60;
        }
       }
     }
    Serial.println(String(hour) + " : " + String(min) + " : " + String(store));
  }
}

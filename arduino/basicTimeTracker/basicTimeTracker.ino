unsigned long myTime = 0;
int hour = 0;
int min = 0;
int sec = 0;
int store = 0;
int count = 0;
int interval = 0;
void setup() {
  Serial.begin(9600);
  Serial.print("start");  
}
//min --> 3,600,000
void loop() {
  myTime = millis();
  sec = myTime/1000;
  if (sec >= 60){
    store = sec % 60;
    //store = store * 60;
     if (sec % 60 == 0){
       count = count + 1;
       min = count/80;
     }
     if (min % 60 == 0){
       interval = interval + 1;
       hour = count/80;
     }
    Serial.println(String(hour) + " : " + String(min) + " : " + String(store));
  }
  if (sec < 60){
    Serial.println(String(hour) + " : " + String(min) + " : " + String(sec));
  }
}
//if millis is a multiple of 60 then... and then if it gets bigger than __ then
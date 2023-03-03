//timer code send to Tera Term

#include <SoftwareSerial.h>// import the serial library
SoftwareSerial MateROV(10, 11); // TX, RX
int BluetoothData; // the data given from Computer


unsigned long myTime = 0;
int hour = 0;
int min = 0;
int sec = 0;
int store = 0;
String addZero = "";
int count = 0;
int interval = 0;
void setup() {
  MateROV.begin(9600);
  MateROV.print("Timer Starts!");  
  //delay(100);
}
//min --> 3,600,000
void loop() {
  if (MateROV.available()){
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
      MateROV.println(String(hour) + " : " + String(min) + " : " + String(store));
    }
    if (sec < 60){
      MateROV.println(String(hour) + " : " + String(min) + " : " + String(sec));
    }
  }
}
//if millis is a multiple of 60 then... and then if it gets bigger than __ then
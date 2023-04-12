#include <SoftwareSerial.h>
SoftwareSerial MegaloDon(10,11); //TX = 10, RX = 11, Ground = Ground, VCC = 5V
int BluetoothData;

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
String companyName = "RN07";
bool isConnected = false;

void setup() {
  Serial.begin(9600);
  MegaloDon.begin(9600);
  connectBluetooth();
  //Serial.println("start");
  Serial.flush();
  while (!Serial.available());
  givenHour = Serial.readStringUntil(',').toInt();
  givenMin = Serial.readStringUntil(',').toInt();
  givenSec = Serial.readStringUntil('.').toInt();
  MegaloDon.println(String(givenHour) + " : " + String(givenMin) + " : " + String(givenSec));

}

void connectBluetooth(){
  while(!isConnected){
    MegaloDon.println("AT");
    //if(MegaloDon.find("OK")){
      isConnected = true;
      MegaloDon.println("Bluetooth ON");
      Serial.println("Connected");
    }
    
      Serial.println("Attempting to reconnect...");
      delay(2000);
    
  }

//min --> 3,600,000
void loop() {
  if(isConnected){
   
  myTime = millis();
  sec = givenSec + (myTime/1000);
  if (sec < 60){
    MegaloDon.println(companyName + " " + String(givenHour) + " : " + String(givenMin) + " : " + String(sec));
  }
  if (sec >= 60){
    store = (sec % 60);
     if (sec % 60 == 0){
       count = count + 1;
       if(count%52 == 0 || count > 52){
        countToMin = count/52;
        mins = givenMin + countToMin;
        hour = givenHour;
        // if(countToMin==2){
        //   mins = mins-2;
        // }
        if(mins%60 ==0){
          mins = 0;
          hour = givenHour + countToMin;
        }
        if(mins > 60){
          mins = mins%60;
        }
       }
     }
    MegaloDon.println(companyName + " " + String(hour) + " : " + String(mins) + " : " + String(store));
  }
  
}else{
  connectBluetooth();
}
}

//to use, plug the USB in, run arduino code with COM6, then run the python code, then open the TeraTerm COM8 port, unplug the USB
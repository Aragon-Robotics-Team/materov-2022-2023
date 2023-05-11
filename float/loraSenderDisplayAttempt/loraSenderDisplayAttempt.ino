#include "LoRaWan_APP.h"
#include "Arduino.h"
// For a connection via I2C using the Arduino Wire include:
#include <Wire.h>               
#include "HT_SSD1306Wire.h"
#include "images.h"

SSD1306Wire  screen(0x3c, 500000, SDA_OLED, SCL_OLED, GEOMETRY_128_64, RST_OLED); // addr , freq , i2c group , resolution , rst

#define DEMO_DURATION 3000
typedef void (*Demo)(void);

int demoMode = 0;
int counter = 1;



#define RF_FREQUENCY                                915000000 // Hz

#define TX_OUTPUT_POWER                             5        // dBm

#define LORA_BANDWIDTH                              0         // [0: 125 kHz,
                                                              //  1: 250 kHz,
                                                              //  2: 500 kHz,
                                                              //  3: Reserved]
#define LORA_SPREADING_FACTOR                       7         // [SF7..SF12]
#define LORA_CODINGRATE                             1         // [1: 4/5,
                                                              //  2: 4/6,
                                                              //  3: 4/7,
                                                              //  4: 4/8]
#define LORA_PREAMBLE_LENGTH                        8         // Same for Tx and Rx
#define LORA_SYMBOL_TIMEOUT                         0         // Symbols
#define LORA_FIX_LENGTH_PAYLOAD_ON                  false
#define LORA_IQ_INVERSION_ON                        false


#define RX_TIMEOUT_VALUE                            1000
#define BUFFER_SIZE                                 30 // Define the payload size here

char txpacket[BUFFER_SIZE];
char rxpacket[BUFFER_SIZE];

double txNumber;

bool lora_idle=true;

static RadioEvents_t RadioEvents;
void OnTxDone( void );
void OnTxTimeout( void );

// 
//#include <TinyGPS++.h>
//#include <SoftwareSerial.h>

static const int RXPin = 4, TXPin = 3;
static const uint32_t GPSBaud = 9600;

// The TinyGPS++ object
//TinyGPSPlus gps;

// The serial connection to the GPS device
//SoftwareSerial ss(RXPin, TXPin);

int givenHour = 19;
double gg = givenHour;
int givenMin = 30;
int givenSec = 0;
int storeMin = 0;
int hour = 0;
int mins = 0;
int sec = 0;
int store = 0;
int count = 0;
int interval = 0;
int countToMin = 0;
String companyName = "RN07";
unsigned long myTime = millis();



void setup() {
    Serial.begin(115200);
//    ss.begin(GPSBaud);
    Mcu.begin();
//  
    txNumber=0;

    RadioEvents.TxDone = OnTxDone;
    RadioEvents.TxTimeout = OnTxTimeout;
    
    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetTxConfig( MODEM_LORA, TX_OUTPUT_POWER, 0, LORA_BANDWIDTH,
                                   LORA_SPREADING_FACTOR, LORA_CODINGRATE,
                                   LORA_PREAMBLE_LENGTH, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   true, 0, 0, LORA_IQ_INVERSION_ON, 3000 ); 

  VextON();
  // delay(100);

  // Initialising the UI will init the display too.
  screen.init();

  screen.setFont(ArialMT_Plain_10);
  
   }



void OnTxDone( void )
{
  Serial.println("TX done......");
  lora_idle = true;
}

void OnTxTimeout( void )
{
    Radio.Sleep( );
    Serial.println("TX Timeout......");
    lora_idle = true;
}

  // myTime = millis();


void drawFontFaceDemo() {
    // Font Demo1
    // create more fonts at http://oledscreen.squix.ch/
    screen.setTextAlignment(TEXT_ALIGN_LEFT);
    screen.setFont(ArialMT_Plain_10);
    sec = givenSec + (myTime/1000);
    if (sec < 60){
    screen.drawString(0, 0, companyName + " - " + (String(givenHour)) + " : " + (String(givenMin)) + " : " + (String(givenSec)));
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
    screen.drawString(0, 0, companyName + " - " + (String(hour)) + " : " + (String(mins)) + " : " + (String(store)));
  }
}

void VextON(void)
{
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext, LOW);
}

void VextOFF(void) //Vext default OFF
{
  pinMode(Vext,OUTPUT);
  digitalWrite(Vext, HIGH);
}


Demo demos[] = {drawFontFaceDemo};
int demoLength = (sizeof(demos) / sizeof(Demo));
long timeSinceLastModeSwitch = 0;

double hehe;
void loop()
{
  if(lora_idle == true)
  {
    // String str;
    //add the timer thing here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // str=String(givenHour);
    // str.toCharArray(b,2);
    //hehe = givenHour;
    // int a = 10, b = 20, c;
    // c = a + b;
    sprintf(txpacket,"The current time is", gg);  //start a package //maybe replace current time as a string that is constantly updated 
    //const char *format
    // const char format[BUFFER_SIZE];
    // format = String(givenHour);
    Serial.printf("\r\nsending packet \"%s\" , length %d\r\n",txpacket, strlen(txpacket));

    Radio.Send( (uint8_t *)txpacket, strlen(txpacket) ); //send the package out 
    lora_idle = false;
  }

 
  screen.clear();
  // draw the current demo method
  demos[demoMode]();

  screen.setTextAlignment(TEXT_ALIGN_RIGHT);
  screen.drawString(10, 128, String(millis()));
  // write the buffer to the display
  screen.display();

  // if (millis() - timeSinceLastModeSwitch > DEMO_DURATION) {
  //   demoMode = (demoMode + 1)  % demoLength;
  //   timeSinceLastModeSwitch = millis();
  // }
  // counter++;
  // delay(10);
    
  Radio.IrqProcess( );
}

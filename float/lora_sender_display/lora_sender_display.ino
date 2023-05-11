//predict a long enough time, upload the sender code, remove sender lora from computer and plug in reciever lora to computer, plug sender lora to float, open serial monitor
//lora sender display and lora receiver are the working hard coded versions of the code that prints to the serial monitor 
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
unsigned long myTime = 0;
int givenHour = 21;
int givenMin = 33;
int givenSec = 55;
int storeMin = 0;
int hour = 0;
int mins = 0;
int sec = 0;
int store = 0;
int count = 0;
int interval = 0;
int countToMin = 0;
String companyName = "RN07";


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
  delay(100);

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



void drawFontFaceDemo() {
    // Font Demo1
    // create more fonts at http://oledscreen.squix.ch/
    screen.setTextAlignment(TEXT_ALIGN_LEFT);
    screen.setFont(ArialMT_Plain_10);
    screen.drawString(0, 0, "RN07 MEGALODON ROV");
}

void drawTextFlowDemo() {
    screen.setFont(ArialMT_Plain_10);
    screen.setTextAlignment(TEXT_ALIGN_LEFT);
    screen.drawStringMaxWidth(0, 0, 128,
      "Lorem ipsum\n dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore." );
}

void drawTextAlignmentDemo() {
  // Text alignment demo
  char str[30];
  int x = 0;
  int y = 0;
  screen.setFont(ArialMT_Plain_10);
  // The coordinates define the left starting point of the text
  screen.setTextAlignment(TEXT_ALIGN_LEFT);
  screen.drawString(x, y, "Left aligned (0,0)");

  screen.drawString(0, 0, "testing testing (0,0)"); //here is where to draw it?? replace first numbers with an x and y and the second with a constantly changing variable


  // The coordinates define the center of the text
  screen.setTextAlignment(TEXT_ALIGN_CENTER);
  x = screen.width()/2;
  y = screen.height()/2-5;
  sprintf(str,"Center aligned (%d,%d)",x,y);
  screen.drawString(x, y, str);

  // The coordinates define the right end of the text
  screen.setTextAlignment(TEXT_ALIGN_RIGHT);
  x = screen.width();
  y = screen.height()-12;
  sprintf(str,"Right aligned (%d,%d)",x,y);
  screen.drawString(x, y, str);
}

void drawRectDemo() {
      // Draw a pixel at given position
    for (int i = 0; i < 10; i++) {
      screen.setPixel(i, i);
      screen.setPixel(10 - i, i);
    }
    screen.drawRect(12, 12, 20, 20);
  
    // Fill the rectangle
    screen.fillRect(14, 14, 17, 17);

    // Draw a line horizontally
    screen.drawHorizontalLine(0, 40, 20);

    // Draw a line horizontally
    screen.drawVerticalLine(40, 0, 20);
}

void drawCircleDemo() {
  for (int i=1; i < 8; i++) {
    screen.setColor(WHITE);
    screen.drawCircle(32, 32, i*3);
    if (i % 2 == 0) {
      screen.setColor(BLACK);
    }
    screen.fillCircle(96, 32, 32 - i* 3);
  }
}

void drawProgressBarDemo() {
  int progress = (counter / 5) % 100;
  // draw the progress bar
  screen.drawProgressBar(0, 32, 120, 10, progress);

  // draw the percentage as String
  screen.setTextAlignment(TEXT_ALIGN_CENTER);
  screen.drawString(64, 15, String(progress) + "%");
}

void drawImageDemo() {
    // see http://blog.squix.org/2015/05/esp8266-nodemcu-how-to-create-xbm.html
    // on how to create xbm files
    screen.drawXbm(34, 14, WiFi_Logo_width, WiFi_Logo_height, WiFi_Logo_bits);
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

// const char* printedItem[100];
String printedItem = "hereerere";
// String hello = "hi";
// char foo[15] ={ hello.c_str()};
// char* bar = foo;
// printedItem = ("\r\n(hour)\r\n ");
//     char foo [100] = printedItem;
//     char*bar = foo;
void loop()
{
  if(lora_idle == true)
  {
    txNumber += 0.01;
    myTime = millis();
  sec = givenSec + (myTime/1000);
  if (sec < 60){
    printedItem = (companyName + " " + String(givenHour) + " : " + String(givenMin) + " : " + String(sec));
  }
  if (sec >= 60){
    store = (sec % 60);
     if (sec % 60 == 0){
       count = count + 1;
       if(count%15 == 0 || count > 15){
        countToMin = count/15;
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
    printedItem = (companyName + " " + String(hour) + " : " + String(mins) + " : " + String(store));
  }
		//sprintf(txpacket,( (const char*)(&givenHour)),txNumber);  //start a package //maybe replace current time as a string that is constantly updated 
      const char *mac=printedItem.c_str();
    sprintf(txpacket,mac,txNumber);
    Serial.printf("\r\nsending packet \"%s\"\r\n",txpacket, strlen(txpacket));

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

  if (millis() - timeSinceLastModeSwitch > DEMO_DURATION) {
    demoMode = (demoMode + 1)  % demoLength;
    timeSinceLastModeSwitch = millis();
  }
  counter++;
  delay(10);
    
  Radio.IrqProcess( );
}

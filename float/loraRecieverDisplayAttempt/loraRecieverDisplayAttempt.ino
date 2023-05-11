#include "LoRaWan_APP.h"
#include "Arduino.h"
#include "HT_SSD1306Wire.h"

SSD1306Wire  screen(0x3c, 500000, SDA_OLED, SCL_OLED, GEOMETRY_128_64, RST_OLED); // addr , freq , i2c group , resolution , rst


#define RF_FREQUENCY                                915000000 // Hz

#define TX_OUTPUT_POWER                             14        // dBm

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

static RadioEvents_t RadioEvents;

int16_t txNumber;
int demoMode = 0;
typedef void (*Demo)(void); 


int16_t rssi,rxSize;

bool lora_idle = true;

void setup() {
    Serial.begin(115200);
    Mcu.begin();
    
    txNumber=0;
    rssi=0;
  
    RadioEvents.RxDone = OnRxDone;
    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetRxConfig( MODEM_LORA, LORA_BANDWIDTH, LORA_SPREADING_FACTOR,
                               LORA_CODINGRATE, 0, LORA_PREAMBLE_LENGTH,
                               LORA_SYMBOL_TIMEOUT, LORA_FIX_LENGTH_PAYLOAD_ON,
                               0, true, 0, 0, LORA_IQ_INVERSION_ON, true );

      screen.init();

  screen.setFont(ArialMT_Plain_10);
}

 uint8_t* payload;
  uint16_t size;
//   // int16_t rssi;
    int8_t snr;
Demo demos[] = {drawFontFaceDemo};
int demoLength = (sizeof(demos) / sizeof(Demo));
long timeSinceLastModeSwitch = 0;

void drawFontFaceDemo(){
  screen.setTextAlignment(TEXT_ALIGN_LEFT);
    screen.setFont(ArialMT_Plain_10);
    screen.drawString(0, 0, "\r\nreceived packet \"%s\" with rssi %d");
}


void loop()
{
  if(lora_idle)
  {
    lora_idle = false;
    Serial.println("into RX mode");
    Radio.Rx(0);
    screen.clear();
  // draw the current demo method
    //demos[demoMode]();
    OnRxDone(payload, size, rssi, snr );
    //     int number = 0;

    // screen.drawString(0,0, ("hi" + String(number)));
    //   number++;
  // screen.setTextAlignment(TEXT_ALIGN_RIGHT);
  // screen.drawString(10, 128, String(millis()));
  // write the buffer to the display
  screen.display();
  }
  Radio.IrqProcess( );
}
bool hereWorks;
void OnRxDone( uint8_t *payload, uint16_t size, int16_t rssi, int8_t snr )
{
    rssi=rssi; //here
    rxSize=size; //here
    memcpy(rxpacket, payload, size );
    rxpacket[size]='\0';
    Radio.Sleep( );
    screen.setTextAlignment(TEXT_ALIGN_LEFT);
    screen.setFont(ArialMT_Plain_10);
    const char datarecieved[40];
    Serial.printf("\r\nreceived packet \"%s\" with rssi %d , length %d\r\n",rxpacket,rssi,rxSize);
    lora_idle = true;
    int number = 0;
    // while(1){
    datarecieved = "\r\nreceived packet \"%s\" with rssi %d";
    screen.drawString(0,0, ("hi"));
    //  number++;
    // }
}
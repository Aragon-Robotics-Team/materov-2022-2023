#include <SPI.h>
#include <LoRa.h>
#include <LiquidCrystal_I2C.h> // Library for LCD
#include "images.h"


LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x26, 20, 4);
void setup()
{

  lcd.init();
  lcd.backlight();

  Serial.begin(9600);
  while (!Serial);
  Serial.println("LoRa Receiver");
  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop()
{

  // try to parse packet

  int packetSize = LoRa.parsePacket();
  lcd.print("hello there");
  if (packetSize)
  {

    // received a paket

    Serial.print("Received packet '");

    lcd.clear();//Added by Railroader

    // read packet

    while (LoRa.available())
    {

      char incoming = (char)LoRa.read();

      if (incoming == 'c')

      {
      }
      else
      {
        lcd.print(incoming);
      }
    }
  }
}

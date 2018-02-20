#include <SPI.h>
#include <WiFi101.h>

char ssid[] = SECRET_SSID;        // your network SSID (name)
int status = WL_IDLE_STATUS;     // the WiFi radio's status


void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
}

void loop() {
  // put your main code here, to run repeatedly:

}

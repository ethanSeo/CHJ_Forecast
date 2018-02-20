#include <SHT1x.h>

#define dataPin 10
#define clockPin 11

SHT1x sht1x(dataPin, clockPin);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp_c;
  float humidity;

  temp_c = sht1x.readTemperatureC();
  humidity = sht1x.readHumidity();

  Serial.print("Temp: ");
  Serial.print(temp_c, DEC);
  Serial.print("\u2103\t");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%\n");
  delay(2000);
}

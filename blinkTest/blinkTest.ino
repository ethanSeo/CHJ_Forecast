int _ledPin = 0;

void setup() {
  // put your setup code here, to run once:
  for(int i=0; i<5; i++){
    pinMode(i, OUTPUT);
  }
}

void blink(int port){
  for(int i=0; i<port; i++){
    digitalWrite(port, HIGH);
    delay(300);
    digitalWrite(port, LOW);
    delay(200);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  blink(_ledPin++);
  if(_ledPin>5){
    _ledPin=0;
  }
}

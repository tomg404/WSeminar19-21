/*
  Signal Generator on ATTiny 13A
  My Arduino IDE Settings: https://i.imgur.com/gAp5znc.png
  Follow this guide for setup: https://create.arduino.cc/projecthub/taunoerik/programming-attiny13-with-arduino-uno-07beba
  W-Seminar Project: "Hacken von Sprachassistenten mithilfe von Laser basierter Audio Injektion"
  (c) Tom Gaimann, 2020
*/


int outputPin = 4;
long period = 1000;

void setup() {
 pinMode(outputPin, OUTPUT);
}

void loop() {
 digitalWrite(outputPin, HIGH);
 delay(period);
 digitalWrite(outputPin, LOW);
 delay(period);
}

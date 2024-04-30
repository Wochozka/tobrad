int ledA = 5;
int ledB = 6;
int brightnessA = 0;
int brightnessB = 255;
int fadeAmount = 5;

void setup() {
  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);
}

void loop() {
  analogWrite(ledA, brightnessA);
  analogWrite(ledB, brightnessB);
  brightnessA = brightnessA + fadeAmount;
  brightnessB = brightnessB - fadeAmount;
  
  if (brightnessA <= 0 || brightnessA >= 255) {
    fadeAmount = -fadeAmount;
  }
  delay(10);
}

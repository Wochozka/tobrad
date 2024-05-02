#define R 3
#define O 4
#define G 5
#define RR 7
#define OO 8
#define GG 9

void setup(){
  pinMode(R, OUTPUT);
  pinMode(O, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(RR, OUTPUT);
  pinMode(OO, OUTPUT);
  pinMode(GG, OUTPUT);
}

void loop(){
  digitalWrite(R, HIGH);
  digitalWrite(O, LOW);
  digitalWrite(G, LOW);
  digitalWrite(RR, LOW);
  digitalWrite(OO, LOW);
  digitalWrite(GG, HIGH);
  delay(2000);
  digitalWrite(O, HIGH);
  digitalWrite(GG, LOW);
  digitalWrite(OO, HIGH);
  delay(1000);
  digitalWrite(R, LOW);
  digitalWrite(O, LOW);
  digitalWrite(G, HIGH);
  digitalWrite(OO, LOW);
  digitalWrite(RR, HIGH);
  delay(2000);
  digitalWrite(O, HIGH);
  digitalWrite(G, LOW);
  digitalWrite(OO, HIGH);
  delay(1000);
  digitalWrite(O, LOW);
  digitalWrite(RR, LOW);
  digitalWrite(OO, LOW);
  digitalWrite(GG, HIGH);
}
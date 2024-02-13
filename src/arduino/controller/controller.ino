#include <Servo.h>

Servo base;
Servo virtualbase;
Servo shoulder;
Servo horizontalshoulder;
Servo horizontalgripper
Servo gripper;

void setup() {
  Serial.begin(9600); 

  base.attach(9)
  virtualbase.attach(10);
  shoulder.attach(8)
  horizontalshoulder.attach(7)
  horizontalgripper.attach(6);
  gripper.attach(5)

  base.write(90)
  shoulder.write(180)

  delay(700)
}

void loop() {
  
  }


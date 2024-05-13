#include <Servo.h>

// Define serv3o objects for each joint
Servo base, shoulder, elbow, wrist, wristRotate, gripper;

// Define servo pin constants
const int basePin = 2, shoulderPin = 3, elbowPin = 4, wristPin = 5, wristRotatePin = 6, gripperPin = 7;

void setup() {
  Serial.begin(9600);

  // Attach each servo to its respective pin
  base.attach(basePin);
  shoulder.attach(shoulderPin);
  elbow.attach(elbowPin);
  wrist.attach(wristPin);
  wristRotate.attach(wristRotatePin);
  gripper.attach(gripperPin);

  // Move servos to initial position
  moveToInitialPosition();
}

void moveToInitialPosition() {
  base.write(60);
  shoulder.write(90);
  elbow.write(130);
  wrist.write(150);
  wristRotate.write(90);
  gripper.write(70);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    executeCommand(command);
  }
}

void executeCommand(String command) {
  if (command == "INITIALIZE") {
    moveToInitialPosition();
  } else if (command.startsWith("MOVE")) {
    handleMovementCommand(command);
  }
}

void handleMovementCommand(String command) {
  // Use strtok to simplify splitting the string
  char input[command.length() + 1];
  command.toCharArray(input, sizeof(input));
  strtok(input, ","); // Skip the first token (the "MOVE" command)
  int pos[6], index = 0;

  while (index < 6) {
    char* token = strtok(NULL, ",");
    if (token == NULL) break;
    pos[index++] = atoi(token);
  }

  // Update servo positions
  base.write(pos[0]);
  shoulder.write(pos[1]);
  elbow.write(pos[2]);
  wrist.write(pos[3]);
  wristRotate.write(pos[4]);
  gripper.write(pos[5]);
}
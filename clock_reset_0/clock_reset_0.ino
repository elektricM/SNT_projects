#include <Servo.h>

// Create a servo object
Servo servoMotor;
Servo Serv;


void setup() {
  // Attach the servo to pin 9
  servoMotor.attach(2); // Change 9 to the desired PWM pin
  Serv.attach(10);
  
  // Set initial position to 0 degrees
  servoMotor.write(0);
  Serv.write(0);
  
}

void loop() {

}

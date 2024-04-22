#include <Wire.h>
#include <Servo.h>

Servo secondsOnes;
Servo secondsTens;
Servo minutesOnes;
Servo minutesTens;
Servo hoursOnes;
Servo hoursTens;

void setup() {
  secondsOnes.write(0); 
  secondsTens.write(0);
  minutesOnes.write(0);
  minutesTens.write(0);
  hoursOnes.write(0);
  hoursTens.write(0);
  
  secondsOnes.attach(2);
  secondsTens.attach(3);
  minutesOnes.attach(4);
  minutesTens.attach(5);
  hoursOnes.attach(6);
  hoursTens.attach(7);

  Serial.begin(9600);
  Serial.println("Seven Segment Clock Begin");
}

void loop() {
  delay(1000); // Delay for one second

  unsigned long currentMillis = millis(); // Get the current time in milliseconds

  // Calculate time components (hours, minutes, seconds)
  unsigned long seconds = (currentMillis / 1000) % 60; // Seconds
  unsigned long minutes = (currentMillis / 60000) % 60; // Minutes
  unsigned long hours = (currentMillis / 3600000) % 24; // Hours (24-hour format)

  Serial.print(hours);
  Serial.print(':');
  Serial.print(minutes);
  Serial.print(':');
  Serial.print(seconds);
  Serial.println();

  // Display seconds
  int curSecsTens = seconds / 10;
  int curSecsOnes = seconds % 10;
  int curSecsTensAngle = curSecsTens * 20;
  int curSecsOnesAngle = curSecsOnes * 20;
  secondsTens.write(curSecsTensAngle);
  secondsOnes.write(curSecsOnesAngle);

  // Display minutes
  int curMinsTens = minutes / 10;
  int curMinsOnes = minutes % 10;
  int curMinsTensAngle = curMinsTens * 20;
  int curMinsOnesAngle = curMinsOnes * 20;
  minutesTens.write(curMinsTensAngle);
  minutesOnes.write(curMinsOnesAngle);

  // Display hours
  int curHoursTens = hours / 10;
  int curHoursOnes = hours % 10;
  int curHoursTensAngle = curHoursTens * 20;
  int curHoursOnesAngle = curHoursOnes * 20;
  hoursTens.write(curHoursTensAngle);
  hoursOnes.write(curHoursOnesAngle);
}

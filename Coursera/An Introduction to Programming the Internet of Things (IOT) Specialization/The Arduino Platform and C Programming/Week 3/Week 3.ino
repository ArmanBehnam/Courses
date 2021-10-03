/*

Write a program that causes the built-in LED connected to pin 13 on the Arduino to blink, 
alternating between fast blinks and slow blinks. The LED should blink 5 times, 
once every half second, and then it should blink 5 more times, once every two seconds. 
The LED should continue to blink in this alternating fashion for as long as the Arduino receives power.

*/

int led = 13;
int i=0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() 
{
  for (i=1;i<=5;i++)
  {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(500);               // wait for a second
  }
  for (i=1;i<=5;i++)
  {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(2000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(2000);               // wait for a second
  }              // wait for a second
}
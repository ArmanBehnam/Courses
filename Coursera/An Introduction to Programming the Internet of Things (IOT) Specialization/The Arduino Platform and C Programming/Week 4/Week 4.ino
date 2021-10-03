/*
Write a program that allows the user to control the LED connected to pin 13 of the Arduino.
When the program is started, the LED should be off.
The user should open the serial monitor to communicate with the Arduino. 
If the user sends the character '1' through the serial monitor then the LED should turn on. If the user sends the character '0' through the serial monitor then the LED should turn off.

*/


// Pin 13 has an LED connected on most Arduino boards.

int led = 13;

// the setup routine runs once when you press reset
void setup() 
{  
// initialize the digital pin as an output.  
pinMode(led, OUTPUT);  
Serial.begin(9600);
}
int state = 0;
void loop() 
{  
if(Serial.available() > 0)  // Checks whether data is comming from the serial port  
{                         
state = Serial.read();  // Reads the data from the serial port  
}  
if (state == '0')  
{  digitalWrite(led, LOW); // Turn LED OFF 
} 
 if (state == '1')  
{  digitalWrite(led, HIGH); // Turn LED ON
}
}
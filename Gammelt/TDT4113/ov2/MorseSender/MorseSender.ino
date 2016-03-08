/* 
 Debounce
 
 Each time the input pin goes from LOW to HIGH (e.g. because of a push-button
 press), the output pin is toggled from LOW to HIGH or HIGH to LOW.  There's
 a minimum delay between toggles to debounce the circuit (i.e. to ignore
 noise).  
 
 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground
 
 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.
 
 
 created 21 November 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Limor Fried
 modified 28 Dec 2012
 by Mike Walters
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/Debounce
 */

// constants won't change. They're used here to 
// set pin numbers:
const int buttonPin = 2;    // the number of the pushbutton pin
const int T = 300;

// Variables will change:
int buttonState;             // the current reading from the input pin
int state = 0;
int lastButtonState = 0;   // the previous reading from the input pin
int currentState;
int lastState;
long lastChange;

// the following variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long lastDebounceTime = 0;  // the last time the output pin was toggled
long timeSinceLastChange = 0;
long dur = 0;
long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);

}

int currentReading() {
  // read the state of the switch into a local variable:
  int reading = digitalRead(buttonPin);

  // check to see if you just pressed the button 
  // (i.e. the input went from LOW to HIGH),  and you've waited 
  // long enough since the last press to ignore any noise:  

  // If the switch changed, due to noise or pressing:
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  } 

  if ((millis() - lastDebounceTime) > debounceDelay) {
    return reading;
  }

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
  lastButtonState = reading;
}

void loop() {
  currentState = currentReading();
  if (currentState != lastState) { 
    timeSinceLastChange = millis() - lastChange;
    lastState = currentState;
    lastChange = millis();

    if (timeSinceLastChange > 2*T && currentState == 0) {
      Serial.println(2);
    } 
    else if (timeSinceLastChange > 0.5*T && currentState == 0) {
      Serial.println(1);
    } 
    else if (timeSinceLastChange > 10*T && currentState == 1) {
      Serial.println(4);
    } 
    else if (timeSinceLastChange > 4*T && currentState == 1) {
      Serial.println(3);
    }

  }
  delay(25);
}


#include <Keypad.h>

const byte ROWS = 4; 
const byte COLS = 4; 

char hexaKeys[ROWS][COLS] = {
  {'D', 'C', 'B', 'A'},
  {'#', '9', '6', '3'},
  {'0', '8', '5', '2'},
  {'*', '7', '4', '1'}
};

byte rowPins[ROWS] = {16, 5, 4, 0}; 
byte colPins[COLS] = {2, 14, 12, 13}; 

Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

String password = "#69420C0C";
String passwordBuffer;

void setup(){
  Serial.begin(9600);                                                                                                                                                                                                                                                                                    
}


void loop(){

  while (true) {
  char customKey = customKeypad.getKey();


  if (customKey == '#') {
      passwordBuffer = ("");
      continue;
  }
  
  if (customKey){
 
    
    Serial.println(customKey);
    passwordBuffer.concat(customKey);
    Serial.println(passwordBuffer);
  }
  }
}

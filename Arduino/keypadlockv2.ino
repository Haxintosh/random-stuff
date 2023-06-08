#include <Keypad.h>
#include <ESP8266WiFi.h>

#define Password_Length 6

#define softAPSSID "softapgobrrr"
#define softAPPSW "die"

int signalPin = 15;

char Data[Password_Length]; 
char Master[Password_Length] = "69420"; 
byte data_count = 0, master_count = 0;
bool Pass_is_good;
char customKey;

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


void setup(){
  WiFi.softAP(softAPSSID, softAPPSW)
  pinMode(signalPin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(signalPin, HIGH);
}

void loop(){

  customKey = customKeypad.getKey();
  Serial.println(customKey);
  if (customKey){
    Data[data_count] = customKey; 
    data_count++; 
    for (int i = 0; i < strlen(Data); i++) {
      Serial.print(Data[i]);
    }
   }

  if(data_count == Password_Length-1){

    if(!strcmp(Data, Master)){
      Serial.println("CORRECT");
      digitalWrite(signalPin, LOW); 
      delay(5000);
      digitalWrite(signalPin, HIGH);
      }
  

    clearData();  
  }
}

void clearData(){
  while(data_count !=0){
    Data[data_count--] = 0; 
  }
  return;
}
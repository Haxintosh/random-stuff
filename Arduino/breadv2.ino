#include <ESP8266WiFi.h>

const char* ssid = "nevergonnegiveyouup";
const char* password = "die";

void setup() {
  Serial.begin(115200);
  
  // Start the Wi-Fi AP
  WiFi.softAP(ssid, password);

  Serial.println("Wi-Fi AP started");
  Serial.print("SSID: ");
  Serial.println(ssid);
  Serial.print("Password: ");
  Serial.println(password);
  
  // Get the IP address of the AP
  IPAddress apIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(apIP);
}

void loop() {
  // Your code here ee
}

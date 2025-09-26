#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "WIFI_SSID";
const char* password = "WIFI_PASS";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected!");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://127.0.0.1:8000/predict");  
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"Berat\":50.2,\"Cahaya\":120,\"R\":200,\"G\":180,\"B\":150,\"Hue\":30,\"Saturation\":0.8,\"Value\":0.9}";
    
    int httpResponseCode = http.POST(jsonData);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Response: " + response);
    } else {
      Serial.println("Error sending POST");
    }
    http.end();
  }
  delay(5000); // kirim tiap 5 detik
}

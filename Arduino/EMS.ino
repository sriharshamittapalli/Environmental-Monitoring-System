#include <SoftwareSerial.h> // Including the software serial library for ESP module, referred from https://docs.arduino.cc/learn/built-in-libraries/software-serial
#include "DHT.h"; // Including DHT.h library for sensing temparature and humidity, referred from https://learn.adafruit.com/dht/using-a-dhtxx-sensor
#define typeOfDhtSensor DHT11 // defining the macro of typeOfDhtSensor
#define dhtDigitalPin 7 // defining the macro of dhtDigitalPin
DHT dhtTempAndHumidity(dhtDigitalPin, typeOfDhtSensor); // sending the required data to dht_temp_and_humidity class
#define receiveDataPin 3
#define transferDataPin 2
const String username = "XXXXXXXXXXXXXX";
const String password = "XXXXXXXXXXXX";
const String apiKey = "TBOC7YZWU6WK2M5S";
const String domainHost = "api.thingspeak.com";
const String portNumber = "80";

int successCountTrueCommand;
int successCountTimeCommand;
boolean detected = false;

SoftwareSerial esp8266WiFiModule(receiveDataPin,transferDataPin);

void setup() {
  dhtTempAndHumidity.begin();
  Serial.begin(9600); //baud rate
  esp8266WiFiModule.begin(115200);
  sendCommand("AT",1,"OK"); // previous val 5
  sendCommand("AT+CWMODE=1",1,"OK"); // Switching to station mode to connect to the Wifi network // previous val 5
  sendCommand(String("AT+CWJAP='") + username + "','" + password + "'", 10, "OK");
  //sendCommand("AT+CWJAP=\""+ username +"\",\""+ password +"\"",20,"OK"); //Connecting ESP8266 to the wifi network by concatinating AT command
  delay(500); // Allowing a timeframe of 800 milliseconds to connect the module to the network
}

void loop() {
  float humidityValue = dhtTempAndHumidity.readHumidity(); // using readHumidity function from DHT library
  float temparatureValue = dhtTempAndHumidity.readTemperature(); // using readTemperature function from DHT library
  float temparatureValueInF = (temparatureValue * 1.8) + 32;
  int airQualityValue = analogRead(A0); // Reading the input from the analog pin 0
  float gasValue = analogRead(A1); // Reading the input from the analog pin 1
  String getEnvironmentalData = "GET https://domainHost/update?api_key="+ apiKey +"&field1="+temparatureValueInF+"&field2="+humidityValue+"&field3="+airQualityValue+"&field4="+gasValue;
  Serial.print("Temperature =" + String(temparatureValueInF) + "°F ");
  Serial.print("Humidity =" + String(humidityValue) + "% ");
  Serial.print("Gas = " + String(gasValue) + " PPM ");
  sendCommand("AT+CIPMUX=1",5,"OK");
  sendCommand("AT+CIPSTART=0,\"TCP\",\""+ domainHost +"\","+ portNumber,15,"OK");
  sendCommand("AT+CIPSEND=0," +String(getEnvironmentalData.length()+4),4,">");
  esp8266WiFiModule.println(getEnvironmentalData);
  delay(1500);
  successCountTrueCommand = successCountTrueCommand+1;
  sendCommand("AT+CIPCLOSE=0",5,"OK");
  delay(500);
}

void sendCommand(String passedCommand, int maximumTime, char scanReplay[]) {
  Serial.print(successCountTrueCommand + ": The Given command -->  " + passedCommand + " ");
  while(successCountTimeCommand < (maximumTime*1)){
    esp8266WiFiModule.println(passedCommand);
    if(esp8266WiFiModule.find(scanReplay)){
      detected = true; break;
    }
    successCountTimeCommand++;
  }
  if(detected){
    Serial.println("Connected Successfully"); successCountTrueCommand++; successCountTimeCommand = 0;
  }else{
    Serial.println("It got Failed"); successCountTrueCommand = 0; successCountTimeCommand = 0;
  }
  detected = false;
 }

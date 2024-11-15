#include <SoftwareSerial.h>
#include <TinyGPS.h>

TinyGPS gps;  //Creates a new instance of the TinyGPS object

float lat = -1.6848579,lon = 37.1690756; 



SoftwareSerial mySerial(9, 10); //RX and TX pins respectively.

void setup()
{
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
  Serial.println("Welcome.");
  Serial.println("......................");
  Serial.println();
  delay(100);
}


void loop()
{
  
  
  if (Serial.available()>0)
   switch(Serial.read())
  {
    case 's':
    case 'S':
      mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
     delay(100);  // Delay of 1 second
     mySerial.println("AT+CMGS=\"916*********0\"\r"); //mobile number to send a text to
     delay(100);
     Serial.println();
     Serial.println("Name: John Doe");
     Serial.println("......................");
     Serial.println("Your location....");
     Serial.println(gps_connect());
     Serial.println("......................");
     Serial.println("Help!!....");
     Serial.println();
     delay(100);
     mySerial.println((char)26);// ASCII code of CTRL+Z for saying the end of sms to  the module 
      delay(1000);
      break;

      
    case 'r':
    case 'R':
      mySerial.println("AT+CNMI=2,2,0,0,0"); // AT Command to receive a live SMS
      delay(100);
      break;
  }

 if (mySerial.available()>0)
   Serial.write(mySerial.read());
}


float gps_connect() {
  while (Serial.available()) { // check for gps data
    if (gps.encode(Serial.read())) // encode gps data
    {
      gps.f_get_position(&lat, &lon); // get latitude and longitude
      // display position

    }
  }

  String latitude = String(lat, 6);
  String longitude = String(lon, 6);
  Serial.println("Latitude: " + latitude + "," "Longitude: " + longitude);
  delay(10);
}

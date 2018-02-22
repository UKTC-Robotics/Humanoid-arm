#include <Servo.h>
const byte numChars = 20;
byte receivedChars[6];
Servo palec,pokazalec,sreden,bezimen, kutre; 
boolean newData = false;
boolean recvInProgress = true;
void setup() {
    Serial.begin(9600);
    Serial.println("<Arduino is ready>");
     palec.attach(A2);
     pokazalec.attach(A3);
     sreden.attach(A4);
     bezimen.attach(A5);
}

void loop() {
    //recvWithStartEndMarkers();
    Serial.readBytes(receivedChars,5);
    delay(10);
    for(int i=0;i<sizeof receivedChars/receivedChars[0];i++)
    {
      map(receivedChars[i],0,100,34,130);
    }
    palec.write(receivedChars[0]);
  Serial.print(receivedChars[0]);
    pokazalec.write(receivedChars[1]);
    Serial.print(int(receivedChars[1]));
    sreden.write(receivedChars[2]);
    Serial.print(int(receivedChars[2]));
    bezimen.write(180-receivedChars[3]);
    Serial.print(int(receivedChars[3]));
    kutre.write(receivedChars[4]);
    Serial.println(int(receivedChars[4]));
    recvInProgress = true;
}

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = 'A';
    char endMarker = 'A';
    char rc;
 
 // if (Serial.available() > 0) {
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("This just in ... ");
        //Serial.println(receivedChars);
        newData = false;
    }
}

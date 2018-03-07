
#include <Servo.h>
String stat;
Servo prusti[5];  
byte pos[5];


void setup() {
  prusti[0].attach(A1);
  prusti[1].attach(A2);
  prusti[2].attach(A0);
  prusti[3].attach(A4);
  prusti[4].attach(A5);
 
  for(int i=0;i<sizeof pos/sizeof pos[0];i++){
    pos[i]=130;
    prusti[i].write(pos[i]);
  }
  Serial.begin(19200);
  Serial.println("I am ready!");
}

void loop() {
 if(Serial.available()>0){
   stat=Serial.readStringUntil(':');
   switch(stat[0]){
     case 'A':pos[0]=130;break;
     case 'a':pos[0]=40;break;
   }
   switch(stat[1]){
     case 'B':pos[1]=40;break;
     case 'b':pos[1]=130;break;
   }
   switch(stat[2]){
     case 'C':pos[2]=25;break;
     case 'c':pos[2]=130;break;
   }
   switch(stat[3]){
     case 'D':pos[3]=50;break;
     case 'd':pos[3]=140;break;
   }
   switch(stat[4]){
     case 'E':pos[4]=60;break;
     case 'e':pos[4]=130;break;
   }
 }

 for(int i=0;i<sizeof pos/sizeof pos[0];i++){
   prusti[i].write(pos[i]);
   Serial.print(pos[i]);
   Serial.print("|");
 }

 Serial.println();
 delay(5);
} 

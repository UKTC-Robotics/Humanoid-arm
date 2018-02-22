import processing.serial.*;
Serial myPort;
void setup(){
  size(600,600);
  try{
  myPort=new Serial(this,"COM8",19200);
  }
  catch(Exception e){
    e.printStackTrace();
  }
}
void draw(){
  background(0,200,0);
  String values[]=loadStrings("myfile.txt");
  textSize(50);
  text(values[values.length-1],200,200);
 // println(values[values.length-1]);
  myPort.write(values[values.length-1]);
  delay(100);
}
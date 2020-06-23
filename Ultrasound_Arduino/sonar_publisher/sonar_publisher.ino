#include <ros.h>
#include <std_msgs/Float64.h>

ros::NodeHandle nh;
std_msgs::Float64 Distance;
ros::Publisher chatter("chatter",&Distance);

int trigPin = 11;      // trig pin of HC-SR04
int echoPin = 12;     // Echo pin of HC-SR04

const int en1 = 5;
const int in11 = 6;
const int in12 = 7;

const int en2 = 8;
const int in21 = 9;
const int in22 = 10;

long duration, distance;


/*void backword(void)
{
  analogWrite(en1, 150);
  digitalWrite(in11,LOW);
  digitalWrite(in12,HIGH);
  
  analogWrite(en2, 150);
  digitalWrite(in21,LOW);
  digitalWrite(in22,HIGH);
  }

void forword(void)
{
  analogWrite(en1, 150);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 150);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
void left(void)
{
  analogWrite(en1, 150);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 0);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
void right(void)
{
  analogWrite(en1, 0);
  digitalWrite(in11,HIGH);
  digitalWrite(in12,LOW);
  
  analogWrite(en2, 150);
  digitalWrite(in21,HIGH);
  digitalWrite(in22,LOW);
  }
void all_stop(void)
{
  analogWrite(en1, 0);
  analogWrite(en2, 0);
  }*/

void setup() {
  Serial.begin(57600); // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  delay(random(500,2000));
 
  pinMode(en1, OUTPUT);
  pinMode(in11, OUTPUT);
  pinMode(in12, OUTPUT);
  
  pinMode(en2, OUTPUT);
  pinMode(in21, OUTPUT);
  pinMode(in22, OUTPUT);
  nh.initNode();
  nh.advertise(chatter);
}

void loop() {

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);   
  digitalWrite(trigPin, HIGH);     // send waves for 10 us
  delayMicroseconds(10);
  duration = pulseIn(echoPin, HIGH); // receive reflected waves
  distance = duration / 58.2;   // convert to distance
  
  Distance.data=distance;
  chatter.publish(&Distance);
  nh.spinOnce();
  delay(10);
    // If you dont get proper movements of your robot then alter the pin numbers
  if (distance > 19)            
  {
    //forword();     
    Serial.println("Moving Ahead");                                           
  }

  if (distance < 18)
  {
    //all_stop();
    Serial.println("STOP");   
    //delay(500);
    //backword();
    //delay(500);
    //all_stop();
    //delay(100);  
    //right();
    //delay(500);
  }

}

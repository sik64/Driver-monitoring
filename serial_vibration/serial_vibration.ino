char cmd;
int S = 9; // use PIN 9 
int S2 = 8 ; // use PIN 8

void setup() {
  
  // 시리얼 통신 시작 (boadrate: 9600)
  Serial.begin(9600);

  pinMode(S, OUTPUT);
	analogWrite(S, 0);

  pinMode(S2, OUTPUT);
	analogWrite(S2, 0);
}

void loop() {

  // 컴퓨터로부터 시리얼 통신이 전송되면, 한줄씩 읽어와서 cmd 변수에 입력
  if(Serial.available()){
    cmd = Serial.read(); 

    if(cmd=='c'){
      //Serial.println("아두이노: c");
      analogWrite(S, 255);
      analogWrite(S2, 255);
      //시리얼 통신으로 입력된 cmd변수가 'c'(closed) 일 경우
      // pin S,S2 (양쪽 진동발생기) 에 ON
      delay(100);
    }
    else if(cmd=='o'){
      //Serial.println("아두이노: o");
      analogWrite(S, 0);
      analogWrite(S2, 0);
      //시리얼 통신으로 입력된 cmd변수가 'o'(open) 일 경우
      // pin S,S2 (양쪽 진동발생기) 에 OFF
      delay(100);
    }
  }
}
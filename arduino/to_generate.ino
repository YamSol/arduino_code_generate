#define led 12
#define 

void setup()
{
  pinMode(12, OUTPUT);

}

void loop()
{

  boolean primeira;
  String strn = "&morse&";

  for(int i=0; i<=strn.length(); i++){
    
    if(strn[i] == '-'){
      digitalWrite(led, HIGH);
      delay(1000);  
    }

    if(strn[i] == '.'){
      digitalWrite(led, LOW);
      delay(1000);
    }
  }
  delay(5000);
}

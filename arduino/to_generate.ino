#define led 12
void setup()
{
  pinMode(12, OUTPUT);
}

void loop()
{

  int bin[] = {&list&};
  boolean primeira;

  for(int i=0; i<=&list_size&; i++){
    
    if(bin[i] == 1){
      digitalWrite(led, HIGH);
      delay(1000);  
    }

    if(bin[i] == 0){
      digitalWrite(led, LOW);
      delay(1000);
    }
  }
  delay(5000);
}

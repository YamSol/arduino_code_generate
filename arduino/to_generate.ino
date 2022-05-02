#define led 12

//times to
#define HYPHEN_COUNT 3
#define DOT_COUNT 1
#define SPACE_COUNT 3
#define SLASHE_COUNT 5

#define DELAY_BASE 400     //ms
#define DELAY_INTERVAL 200 //ms

void setup()
{
  pinMode(12, OUTPUT);
}

boolean primeira;
String strn = "&morse&";

void loop()
{
  if (primeira)
  {

    for (int i = 0; i <= strn.length(); i++)
    {

      if (strn[i] == '-')
      {
        digitalWrite(led, HIGH);
        delay(DELAY_BASE * HYPHEN_COUNT);
      }

      else if (strn[i] == '.')
      {
        digitalWrite(led, HIGH);
        delay(DELAY_BASE * DOT_COUNT);
      }

      else if (strn[i] == ' ')
      {
        digitalWrite(led, LOW);
        delay(DELAY_BASE * SPACE_COUNT);
      }

      else if (strn[i] == '/')
      {
        digitalWrite(led, LOW);
        delay(DELAY_BASE * SLASHE_COUNT);
      }

      digitalWrite(led, LOW);
      delay(DELAY_INTERVAL);
    }
    primeira = false;
  }
  delay(5000);
}
// glitch effect for 7 segment leds and 2 leds
// for an insect, 2 of the leds are the eyes 
#define LEFT_EYE 26
#define RIGHT_EYE 12

#define SEGMENT_A 17 // top segment
#define SEGMENT_B 0 // top right segment
#define SEGMENT_C 2 // bottom right segment
#define SEGMENT_D 25 // bottom segment
#define SEGMENT_E 33 // bottom left segment
#define SEGMENT_F 19 // top left segment
#define SEGMENT_G 23 // middle segment
#define SEGMENT_DP 15 // dot segment

#define DELAY 100

const int cycleCount = 100; // Number of cycles before settling to HIGH

// Variables
int cycle = 0;

void setup() {
  // initialize the digital pin as an output.
  pinMode(LEFT_EYE, OUTPUT);
  pinMode(RIGHT_EYE, OUTPUT);
  pinMode(SEGMENT_A, OUTPUT);
  pinMode(SEGMENT_B, OUTPUT);
  pinMode(SEGMENT_C, OUTPUT);
  pinMode(SEGMENT_D, OUTPUT);
  pinMode(SEGMENT_E, OUTPUT);
  pinMode(SEGMENT_F, OUTPUT);
  pinMode(SEGMENT_G, OUTPUT);
  pinMode(SEGMENT_DP, OUTPUT);
}

void loop() {
  if (cycle < cycleCount) {
    // Generate a random delay between 50ms to 500ms
    int randomDelay = random(10, 200);

    // Set LED to a random state (HIGH or LOW)
    digitalWrite(SEGMENT_A, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_B, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_C, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_D, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_E, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_F, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_G, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_DP, random(2) == 0 ? LOW : HIGH);
    digitalWrite(LEFT_EYE, random(2) == 0 ? LOW : HIGH);
    digitalWrite(RIGHT_EYE, random(2) == 0 ? LOW : HIGH);
    
    // Wait for the random delay
    delay(randomDelay);

    // Increment the cycle count
    cycle++;
  } else {
    digitalWrite(SEGMENT_A, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_B, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_C, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_D, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_E, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_F, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_G, random(2) == 0 ? LOW : HIGH);
    digitalWrite(SEGMENT_DP, random(2) == 0 ? LOW : HIGH);
    digitalWrite(LEFT_EYE, HIGH);
    digitalWrite(RIGHT_EYE, HIGH);
    delay(random(10, 200));
  }
}

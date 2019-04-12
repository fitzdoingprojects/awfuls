/* Awful's Gas and Snack */
/* Blame everything on Fitz */
/* 190411 */

/*
button mapping on header from keypad
1	ka1 11, 6 
2	ka2 11, 7 
3	ka3 11, 8
can ka4 11, 9

4	kb1 4, 6
5	kb2 4, 7
6	kb3 4, 8
clr	kb4 4, 9

7	kc1 5, 6
8	kc2 5, 7
9	kc3 5, 8

*	kd1 10, 6
0	kd2 10, 7Serial.print
#	kd3 10, 8
ent	kd4 10, 9

mapping from header to arduino:
	MAP 11 to pin 10, 4 to pin 11, 5 to pin 12, 10 to 13
	keep 6-9 mapped to themselves
*/

#define ROW_LEN 4
#define COL_LEN 4

int row[4] = {10, 11, 12, 13};
int col[4] = {6, 7, 8, 9};

char button[ROW_LEN][COL_LEN] = {  
	{'1', '2', '3', 'X'} ,   /*  initializers for row indexed by a */
	{'4', '5', '6', '<'} ,   /*  initializers for row indexed by b */
	{'7', '8', '9', 0},   /*  initializers for row indexed by c */
	{'*', '0', '#', 'E'}   /*  initializers for row indexed by d */
};


void setup() {
	//start serial connection
	Serial.begin(9600);

	Serial.println("START UP...");
	
	//configure pin 2 as an input and enable the internal pull-up resistor
	for(uint8_t i = 0; i < ROW_LEN; i++) {
		pinMode(row[i], OUTPUT);
	}

	for(uint8_t i = 0; i < ROW_LEN; i++) {
		pinMode(col[i], INPUT_PULLUP);
	}
}

void reset_rows() {
	for(uint8_t i = 0; i < ROW_LEN; i++) {
		 digitalWrite(row[i], 1);
	}
}

bool pressed(uint8_t button) {
	/* TODO: maybe add debouncing??? */
	if(digitalRead(button) == 0) {
		return true;
		
	}
	return false;
}

void loop() {
	for(uint8_t i = 0; i < ROW_LEN; i++) {
		reset_rows();
		digitalWrite(row[i], 0);
		for(uint8_t j = 0; j < COL_LEN; j++) {
			delay(5);
			if(pressed(col[j])) {
				Serial.println(button[i][j]);
			}
		}
	}
}

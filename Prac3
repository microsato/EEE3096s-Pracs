//jo  GNU nano 3.2                                                                                        BinClock.c
#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <stdio.h> //For printf functions
#include <stdlib.h> // For system functions
#include <math.h>
#include "BinClock.h"
#include "CurrentTime.h"

//Global variables
int hours, mins, secs;
long lastInterruptTime = 0; //Used for button debounce
int RTC; //Holds the RTC instance

int HH,MM,SS;
const int HLED[]={7,3,4,5}; //hours LEDs (wiringPi)
const int MLED[]={6,25,24,23,22,21};// Minutes LEDs (wiringPi)
void initGPIO(void){
        
        printf("Setting up\n");
        wiringPiSetup(); //This is the default mode. If you want to change pinouts, be aware

        RTC = wiringPiI2CSetup(RTCAddr); //Set up the RTC

        //Set up the LEDS
        for(int i; i < sizeof(LEDS)/sizeof(LEDS[0]); i++){
            pinMode(LEDS[i], OUTPUT);
        }

        //Set Up the Seconds LED for PWM
        pinMode(1,PWM_OUTPUT);
        printf("LEDS done\n");
//Set up the Buttons
        for(int j=0; j < sizeof(BTNS)/sizeof(BTNS[0]); j++){
                pinMode(BTNS[j], INPUT);
                pullUpDnControl(BTNS[j], PUD_UP);
                //printf("LED done");
        }

        // set the button interrupts
        wiringPiISR (0, INT_EDGE_FALLING,hourInc);
        wiringPiISR (2, INT_EDGE_FALLING, minInc);


        printf("BTNS done\n");
        printf("Setup done\n");
}


int main(void){
        initGPIO();

        //Set random time (3:04PM)
        //You can comment this file out later
        wiringPiI2CWriteReg8(RTC, HOUR, 0x1);
        wiringPiI2CWriteReg8(RTC, MIN, 0x3);
        wiringPiI2CWriteReg8(RTC, SEC, 0b10000000);

        // Repeat this until we shut down
        for (;;){
                //Fetch the time from the RTC
                SS=wiringPiI2CReadReg8(RTC, SEC);
                MM=wiringPiI2CReadReg8(RTC, MIN);
                HH=wiringPiI2CReadReg8(RTC, HOUR);
                //Function calls to toggle LEDs
                SS=SS-0x80;
                printf("Hex: %x:%x:%x\n", HH, MM, SS);
                HH= hFormat(HH);
                lightMins(MM);
                lightHours(HH);
//Write your logic here
                secPWM(SS);
                HH = decCompensation(HH);
                // Print out the time we have stored on our RTC
                printf("The current time is: %x:%x:%x\n", HH, MM, SS);

                //using a delay to make our program "less CPU hungry"
                delay(900); //milliseconds
        }
        return 0;
}

/*
 * Change the hour format to 12 hours
 */
int hFormat(int hours){
        /*formats to 12h*/
        hours = hexCompensation(hours); //changes to decimal
        if (hours >= 24){
                hours = 0;
        }
        else if (hours > 12){
                hours -= 12;
        }
        return (int)hours;
}

void lightHours(int units){
        // Write your logic to light up the hour LEDs here
        int temp = units;
        int rem=0;
        int bin[]={0,0,0,0};
        for (int i=0; i<=3; i++){
                rem= temp%2;
                temp=temp/2;
                bin[i]=rem;
	}
for (int i=0; i<=5;i++){
                digitalWrite(MLED[i], bin[i]);
        }
}
void secPWM(int units){
        //100/60=1.67. 1.67*SS= output Duty cycle
        int out =hexCompensation(units); 
        out=1.67*out;
        pwmWrite(1,out);
}

int hexCompensation(int units){
        /*Convert HEX or BCD value to DEC where 0x45 == 0d45
          This was created as the lighXXX functions which determine what GPIO pin to set HIGH/LOW
          perform operations which work in base10 and not base16 (incorrect logic)
        */
        int unitsU = units%0x10;

        if (units >= 0x50){
                units = 50 + unitsU;
        }
        else if (units >= 0x40){
        	units = 40 + unitsU;
        }
        else if (units >= 0x30){
                units = 30 + unitsU;
        }
        else if (units >= 0x20){
                units = 20 + unitsU;

        }
        else if (units >= 0x10){
                units = 10 + unitsU;
        }
        return units;
}


/*
 * decCompensation
 * This function "undoes" hexCompensation in order to write the correct base 16 value through I2C
 */

int decCompensation(int units){
        int unitsU = units%10;

        if (units >= 50){
                units = 0x50 + unitsU;
        }
        else if (units >= 40){
                units = 0x40 + unitsU;
        }
        else if (units >= 30){
                units = 0x30 + unitsU;
        }
        else if (units >= 20){
                units = 0x20 + unitsU;
        }
        else if (units >= 10){
                units = 0x10 + unitsU;
        }
        return units;
}

void hourInc(void){
        //Debounce
        long interruptTime = millis();
        if (interruptTime - lastInterruptTime>200){
                printf("Interrupt 1 triggered, %x\n", hours);
                       //Fetch RTC Time

                HH=wiringPiI2CReadReg8(RTC, HOUR);
                HH= hexCompensation(HH);
                //Increase hours by 1, ensuring not to overflow
                if(HH==12){
                        HH=1;
                        }
                else HH+=1;
                HH=decCompensation(HH);
                //Write hours back to the RTC
                wiringPiI2CWriteReg8(RTC, HOUR, HH);
 }

        lastInterruptTime = interruptTime;
}

void minInc(void){
        long interruptTime = millis();

        if (interruptTime - lastInterruptTime>200){
                printf("Interrupt 2 triggered, %x\n", mins);
                //Fetch RTC Time
                MM=wiringPiI2CReadReg8(RTC, MIN);
                MM=hexCompensation(MM);
                //Increase minutes by 1, ensuring not to overflow
                if(MM==59){
                        MM=0;
  		}
                else MM=MM+1;
                MM=decCompensation(MM);
                //Write minutes back to the RTC

        wiringPiI2CWriteReg8(RTC, MIN, MM);

        }
        lastInterruptTime = interruptTime;
}


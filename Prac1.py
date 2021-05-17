
#!/usr/bin/python3
"""
Python Practical Template
K. Cranky
Readjust this Docstring as follows:
Names:  Mic Rosato
Student Number: RSTMIC005
Prac: Prac1
Date: 26/07/19
"""

# import Relevant Librares
import RPi.GPIO as GPIO
from itertools import product

#constants and global variables
counter = 0 #global counter

#setup GPIO pins
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) #use BCM numbering of pins
GPIO.setup(17,GPIO.OUT) #LED 1
GPIO.setup(27,GPIO.OUT) #LED 2
GPIO.setup(22,GPIO.OUT) #LED 3

GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP) #SW1 (inc) - internal pull up res
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP) #SW2 (dec) - internal pull up res 
GPIO.remove_event_detect(6) #remove past interrupts sw1
GPIO.remove_event_detect(5) #remove past interrupts sw2

LED_Pins = [17,27,22] #array of LED pins

comb = list(product([1,0],repeat=3)) #create binary list (1,1,1) -> (0,0,0) 

arr=comb[::-1] #reverse comb list so that (0,0,0) -> (1,1,1) 

def main(): #continously runs
        GPIO.setwarnings(False) 
def incriment(channel): #interrupt sw1
        global counter 
        if (counter == 7): #if LEDs all on-counter full
                counter = 0 #reset the counter 
        else:
                counter=counter+1 #incriment counter by 1
        LEDs_On() #display current counter value on LEDs

def decriment(channel):
        global counter
        if (counter == 0): #if counter empty
                counter=7 #loop around counter - full 
        else:
                counter=counter-1 #decriment counter by 1
        LEDs_On() #display current counter value on LEDs

def LEDs_On():
        GPIO.output(LED_Pins,arr[counter]) #correspond LED pin to counter pos in binary array


GPIO.add_event_detect(6,GPIO.FALLING,callback=incriment,bouncetime=250) #sw1 interrupt- falling edge, incriments counter , debounce time 250ms
GPIO.add_event_detect(5,GPIO.FALLING,callback=decriment,bouncetime=250)#sw2 interrupt- falling edge, decriments counter , debounce time 250ms


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
        GPIO.cleanup()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)


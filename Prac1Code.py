
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
counter = 0

#setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP) #sw pin5  dec
GPIO.remove_event_detect(6)
GPIO.remove_event_detect(5)

LED_Pins = [17,27,22]

comb = list(product([1,0],repeat=3))

arr=comb[::-1]

def main():
        GPIO.setwarnings(False)
def incriment(channel):
        global counter
        if (counter == 7):
                counter = 0 #reset the counter
        else:
                counter=counter+1 #incriment counter by 1
        LEDs_On()

def decriment(channel):
        global counter
        if (counter == 0):
                counter=7
        else:
                counter=counter-1 #decriment counter by 1
        LEDs_On()

def LEDs_On():
        GPIO.output(LED_Pins,arr[counter])


GPIO.add_event_detect(6,GPIO.FALLING,callback=incriment,bouncetime=250)
GPIO.add_event_detect(5,GPIO.FALLING,callback=decriment,bouncetime=250)


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


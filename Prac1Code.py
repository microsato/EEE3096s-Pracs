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
#constants and global variables

#setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

GPIO.setup(5,GPIO.IN,pull_up_down=GPIO.PUD_UP) #set button as input, pull up resistors - when pressed goes low
GPIO.remove_event_detect(5) #initially remove all previous events


def main():
        GPIO.setwarnings(False)

def LightUp(channel):
        GPIO.output(17,1) #turn on LED
	time.sleep(3) #wait for 3s
	GPIO.output(17,0) #turn LED off

GPIO.add_event_detect(5,GPIO.FALLING,callback=LightUp,bouncetime=250) #interrupt on falling edge (when pressed) + debounce time 250ms 


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


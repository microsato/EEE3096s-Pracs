

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
import time
#constants and global variables

#setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #read pins as BCM numbers 
GPIO.setup(26,GPIO.OUT) #set pin 17 as output pin


def main():

	while (True):
		GPIO.output(26,1) #turn LED on (high) 
		time.sleep(0.5) #delay 0.5s 
		GPIO.output(26,0) #turn LED off(low) 
		time.sleep(0.5)
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
    #except e:
     #   GPIO.cleanup()
      #  print("Some other error occurred")
       # print(e.message)



"""***************************************************************************
LED_Example.py

Description:
  Sample Python code for interfacing an LED to Raspberry Pi

Tutorial Link:  
  http://learn.edwinrobotics.com/Getting-Started-with-Raspberry-Pi-and-Electronics/

Created
Abhishek Nair @ Edwin Robotics
Feb 6th 2017

Distributed as-is; no warranty is given.   
****************************************************************************"""

#**************Import Libraries ***********************************************
import time                 # Time library to add delay to the program
import RPi.GPIO as GPIO     # This library defines how to work with Raspberry Pi GPIO Pins
#******************************************************************************


#*****************Parameters **************************************************
GPIO.setmode(GPIO.BCM)      # This will set the pin naming convention to BCM option means that you are referring to the pins by the "Broadcom SOC channel" number, the other naming convention is GPIO.BOARD which will refer the Physical pin numbers on the board.
GPIO.setwarnings(False)     # Set Python not to print GPIO warning messages to the screen
#******************************************************************************


#*******************Define*****************************************************
led = 23                    # Defines the GPIO Pin number 23 as led, now if you call led in the Code it will refer to Pin 23
#******************************************************************************


#*******Set GPIO Pins as INPUT/OUTPUT******************************************
GPIO.setup(led,GPIO.OUT)    # Set led as output
#******************************************************************************


#***********Main Code Begins Here**********************************************

While True: 
  print("LED ON")             # Print Message "LED ON" to the screen
  GPIO.output(led,GPIO.HIGH)  # Set led pin High (i.e Set it to 3.3 Volt)

  time.sleep(5)               # Set the code to sleep for 5 seconds before proceeding to next line

  print("LED OFF")            # Print Message "LED OFF" to the screen
  GPIO.output(led,GPIO.LOW)   # Set led pin Low (i.e Set it to 0 Volt)

  GPIO.cleanup()              # This command reset the status of any GPIO pins when you exit the program. If you don’t use this, then the GPIO pins will remain at whatever state they were last set to.

#*******************END*********************************************************
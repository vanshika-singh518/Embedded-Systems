# program to switch a high-power DC device using relay.

# import modules
import RPi.GPIO as GPIO
from time import sleep
 
# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
 
while True:
  x = input("on/off/exit")
  if x == "on" or x == "ON":
    GPIO.output(18, GPIO.HIGH)
    sleep(0.5)
    
  if x == "off" or x == "OFF":
    GPIO.output(18, GPIO.LOW)
    sleep(0.5)
    
  if x == "exit" or x == "EXIT":
    break
    
  GPIO.cleanup()

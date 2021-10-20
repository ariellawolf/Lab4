#!/usr/bin/python3
# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output
import RPi.GPIO as GPIO
import time
import json

ledPin1= 13
ledPin2= 19
ledPin3= 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)
pwm1= GPIO.PWM(ledPin1, 100)
pwm2= GPIO.PWM(ledPin2, 100)
pwm3= GPIO.PWM(ledPin3, 100)

# PWM object on our pin at 100 Hzpwm.start(0)
# start with LED off
while True:
  with open('led-pwm.txt', 'r') as f:
    dataRead= json.load(f) # read duty cycle value from file
    dutyCycle = float(dataRead['slider'])
    LED = float(dataRead['light'])
  if LED ==1:
    pwm1.ChangeDutyCycle(dutyCycle)
  elif LED == 2:
    pwm2.ChangeDutyCycle(dutyCycle)
  elif LED == 3:
    pwm3.ChangeDutyCycle(dutyCycle)
  else:
    break

  time.sleep(0.1)

GPIO.cleanup()
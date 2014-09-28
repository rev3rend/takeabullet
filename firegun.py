# take a bullet for this city
# stepper controller (non-interactive)

import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

coil_A_1_pin = 23
coil_A_2_pin = 18
coil_B_1_pin = 22
coil_B_2_pin = 17

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def forward(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)

def backward(delay, steps):
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

def fire():
  print("Python Firing Gun!!!")
  steps = 20
  delay = 5/1000.0
  setStep(0, 0, 0, 0)
  forward(delay,steps)
  #steps = 7
  backward(delay,steps)
  setStep(0, 0, 0, 0)

fire()

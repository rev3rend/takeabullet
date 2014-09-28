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

def main():
  steps = 10
  delay = 5/1000.0
  setStep(0, 0, 0, 0)
  while True:
    dir_in = raw_input("f/b/q:\n")
    if dir_in.lower() == 'f':
      forward(delay,steps)
      setStep(0, 0, 0, 0)
    elif dir_in.lower() == 'b':
      backward(delay,steps)
      setStep(0, 0, 0, 0)
    elif dir_in.lower() == 's':
      setStep(1, 0, 0, 1)
      time.sleep(delay)
      setStep(0, 1, 0, 1)
    elif dir_in.lower() == 'l':
      setStep(0, 0, 0, 0)
    elif dir_in.lower() == 'a':
      backward(delay,steps)
      forward(delay,steps)
      setStep(0, 0, 0, 0)
    elif dir_in.lower() == 'q':
      setStep(0, 0, 0, 0)
      break

main()
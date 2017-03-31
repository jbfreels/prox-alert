import pygame
import glob
import random
import RPi.GPIO as gpio
import time

PIN_TRIGGER = 16          # trigger
PIN_ECHO = 18             # echo
MAX_TRIGGER_DISTANCE = 1  # in meters, max is ~3

def setup_init():
  pygame.mixer.init()
  gpio.setmode(GPIO.BOARD)
  gpio.setup(PIN_TRIGGER, gpio.OUT, initial=gpio.LOW)
  gpio.setup(PIN_ECHO, gpio.IN)
  time.sleep(1)

def check_dist():
  gpio.output(PIN_TRIGGER, gpio.HIGH)
  time.sleep(0.000015)
  gpio.output(PIN_TRIGGER, gpio.LOW)
  while not gpio.input(PIN_ECHO):
    pass
  t1 = time.time()
  while gpio.input(PIN_ECHO): # wait for echo
    pass
  t2 = time.time()
  return (t2-t1)*340/2        # return distance in meters

def do_fart():
  pygame.mixer.music.load(random.choice(farts))
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy() == True:
    continue

farts = glob.glob('./snd/*.mp3')  # collect sounds
setup_init()

try:
  while True:
    if check_dist() < MAX_TRIGGER_DISTANCE:
      do_fart()
      print 'Who farted?'
      time.sleep(60)        # wait a minute before repeat
except KeyboardInterrupt:
  gpio.cleanup()            # cleanup and die on CTRL-C
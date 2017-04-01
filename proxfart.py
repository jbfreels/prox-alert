"""
This is a sample for a Raspberry Pi connected to a Prallax
PING sensor.  When the sensor is triggered, a sound will play.

Run:
python proxfart.py

Stop:
CTRL-C
"""
import glob
import random
import time
import pygame
import RPi.GPIO as gpio

PIN_TRIGGER = 16          # trigger
PIN_ECHO = 18             # echo
MAX_TRIGGER_DISTANCE = 1  # in meters, max is ~3

def setup_init():
    """Initualize GPIO"""
    pygame.mixer.init()
    gpio.setmode(GPIO.BOARD)
    gpio.setup(PIN_TRIGGER, gpio.OUT, initial=gpio.LOW)
    gpio.setup(PIN_ECHO, gpio.IN)
    time.sleep(1)


def check_dist():
    """Check sensor distance
    :return: distance in meters
    """
    gpio.output(PIN_TRIGGER, gpio.HIGH)
    time.sleep(0.000015)
    gpio.output(PIN_TRIGGER, gpio.LOW)
    while not gpio.input(PIN_ECHO):
        pass
    timetrig = time.time()
    while gpio.input(PIN_ECHO):  # wait for echo
        pass
    timeecho = time.time()
    return (timeecho - timetrig) * 340 / 2        # return distance in meters

def do_fart():
    """Play random sound from glob"""
    pygame.mixer.music.load(random.choice(FARTS))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

if __name__ == '__main__':
    FARTS = glob.glob('./mp3/*.mp3')  # collect sounds
    setup_init()

    try:
        while True:
            if check_dist() < MAX_TRIGGER_DISTANCE:
                do_fart()
                print 'Who farted?'
                time.sleep(60)        # wait a minute before repeat
    except KeyboardInterrupt:
        gpio.cleanup()            # cleanup and die on CTRL-C

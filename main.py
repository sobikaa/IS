
# THAPA SOBIKA, SENIOR IS
# This file plays the sound and LEDs based on the user's touch

from sound_functions import *

import MPR121
from gpiozero import RGBLED
import RPi.GPIO as GPIO
import time
import subprocess
import pygame
from pygame.mixer import Sound
from glob import glob
from time import sleep

sensor = MPR121.begin()

# set the threshold so the PiCap can sense the touch
sensor.set_touch_threshold(20)
sensor.set_release_threshold(10)

led = RGBLED(6, 5, 26, active_high=False)
led.blue = 1
subprocess.call("picap-samples-to-wav tracks", shell=True)
led.off()

# initialize mixer and pygame
pygame.mixer.pre_init(frequency=44100, channels=64, buffer=1024)
pygame.init()

# list of sounds to call out the appliance name
audio_labels = [Sound(path) for path in sorted(glob("label_tracks/.wavs/TRACK*.wav"))]

counter = 0  # counter variable to activate one appliance at a time
def increment():
    global counter

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        if sensor.is_new_touch(11):

            while True:
                counter += 1
                print("count = " + str(counter))

                if counter % 8 == 0:
                    counter = 1

running = True

while running:

    try:
        increment()
            audio_label[0].play()

        if (counter == 1):
            audio_label[1].play()
            trumpet()

        if (counter == 2):
            audio_label[2].play()
            xylophone()

        if (counter == 3):
            audio_label[3].play()
            harp()

        if (counter == 4):
            audio_label[4].play()
            flute()

        if (counter == 5):
            audio_label[5].play()
            drum()

        if (counter == 6):
            audio_label[6].play()
            music_playlist()

        if (counter == 7):
            audio_label[7].play()
            animals()

    except KeyboardInterrupt:
        led.off()
        running = False
        sleep(1)

# THAPA SOBIKA, SENIOR INDEPENDENT STUDY
# This file contains the sounds used for the project. Alongside, there are functions for each musical appliance.

#sound tracks for each appliance
trumpet_sound = [Sound(path) for path in sorted(glob("trumpet_tracks/.wavs/TRACK*.wav"))]
xylophone_sound = [Sound(path) for path in sorted(glob("xylophone_tracks/.wavs/TRACK*.wav"))]
harp_sound = [Sound(path) for path in sorted(glob("harp_tracks/.wavs/TRACK*.wav"))]
flute_sound = [Sound(path) for path in sorted(glob("flute_tracks/.wavs/TRACK*.wav"))]
drum_sound = [Sound(path) for path in sorted(glob("drum_tracks/.wavs/TRACK*.wav"))]
playlist_songs = [Sound(path) for path in sorted(glob("playlist_tracks/.wavs/TRACK*.wav"))]
animal_sounds = [Sound(path) for path in sorted(glob("animals_tracks/.wavs/TRACK*.wav"))]

# Instruments
# This function is used to activate the LED near the trumpet and allows users to play the trumpet when they touch
# on the black areas
def trumpet():

    LED_PIN = 16  # setting GPIO 16 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 2):

            if sensor.get_touch_data(i):
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                is_any_touch_registered = True
                sound = trumpet_sound[i]
                sound.play()  # plays the sound according to the touch

        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()


# This function is used to activate the LED near the xylophone and allows users to play the trumpet when they touch
# on the black areas
def xylophone():

    LED_PIN = 25  # setting GPIO 25 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 6):

            if sensor.get_touch_data(i):
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                is_any_touch_registered = True
                sound = xylophone_sound[i]
                sound.play()  # plays the sound according to the touch

        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()

# This function is used to activate the LED near the harp and allows users to play the trumpet when they touch
# on the black areas
def harp():

    LED_PIN = 24  # setting GPIO 24 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 7):

            if sensor.get_touch_data(i):
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                is_any_touch_registered = True
                sound = harp_sound[i]
                sound.play()  # plays the sound according to the touch

        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()

# This function is used to activate the LED near the flute and allows users to play the trumpet when they touch
# on the black areas
def flute():

    LED_PIN = 23  # setting GPIO 23 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 6):

            if sensor.get_touch_data(i):
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                is_any_touch_registered = True
                sound = flute_sound[i]
                sound.play()  # plays the sound according to the touch

        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()

# This function is used to activate the LED near the drum and allows users to play the trumpet when they touch
# on the black areas
def drum():

    LED_PIN = 22  # setting GPIO 22 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 6):

            if sensor.get_touch_data(i):
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                is_any_touch_registered = True
                sound = drum_sound[i]
                sound.play()  # plays the sound according to the touch

        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()

#music_playlists

# This function is used to activate the LED near the music genre names and allows users to play the trumpet when they touch
# on the black areas
def music_playlist():

    LED_PIN = 18  # setting GPIO 18 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 9):

            if sensor.get_touch_data(i):
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                is_any_touch_registered = True
                sound = playlist_songs[i]
                sound.play()  # plays the sound according to the touch

                if sensor.touch_status_changed():
                    sensor.update_touch_data()

                    if sensor.is_new_touch(10):
                        sound.pause()  # pauses the currently playing song


        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()


#animals
# This function is used to activate the LED near the pictures of animals and allows users to play the trumpet when they touch
# on the black areas
def animals():

    LED_PIN = 27 #setting GPIO 27 to the LED

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # activate the LED

    if sensor.touch_status_changed():  # returns the MPR status so the touch data updates
        sensor.update_touch_data()

        is_any_touch_registered = False

        for i in range(0, 8):

            if sensor.get_touch_data(i):
                is_any_touch_registered = True
                # register the touch so PiCap LED turns on. This is to make sure that PiCap sensed the touch.
                sound = animal_sounds[i]
                sound.play()  # plays the sound according to the touch

        if is_any_touch_registered:
            led.red = 1
        else:
            led.off()

    GPIO.output(LED_PIN, GPIO.LOW)  # turn the LED off
    GPIO.cleanup()
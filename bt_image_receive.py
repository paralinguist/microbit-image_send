from microbit import *
import radio

#Turns on the bluetooth radio. FYI: this will drain the battery faster than normal operations.
radio.on()

#An infinite loop
while True:
    #Listen for a bluetooth broadcast and save it to a string.
    image = radio.receive()
    #Check that the string is set to a value.
    if image is not None:
        i = Image(image)
        display.show(i)
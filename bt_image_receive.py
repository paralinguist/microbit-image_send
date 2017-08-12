from microbit import *
import radio

radio.on()

while True:
    image = radio.receive()
    if image is not None:
        i = Image(image)
        display.show(i)
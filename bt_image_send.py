from microbit import *
import radio

def image_to_string(source):
    target = str(source)
    target = target.replace("Image(","")
    target = target.replace("\n", "")
    target = target.replace("'", "")
    target = target.replace(" ", "")
    target = target.replace(")", "")
    target = target[:-1]
    return target
    
images = [Image.ANGRY, Image.ASLEEP, Image.CHESSBOARD, Image.CONFUSED, Image.COW, Image.FABULOUS, Image.GHOST]
image_number = -1

while True:
    if button_a.was_pressed():
        image_number = image_number + 1
        if image_number >= len(images):
            image_number = 0
        display.show(images[image_number])
    if button_b.was_pressed():
        message = image_to_string(images[image_number])
        radio.on()
        radio.send(message)
    sleep(50)
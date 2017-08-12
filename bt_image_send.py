from microbit import *
import radio

#Simple function to turn built-in images to strings - parameter is a built-in image object
def image_to_string(source):
    #Convert the image to a string.
    target = str(source)
    #Format the string as a custom image string.
    target = target.replace("Image(","")
    target = target.replace("\n", "")
    target = target.replace("'", "")
    target = target.replace(" ", "")
    target = target.replace(")", "")
    #Slice off the last character.
    target = target[:-1]
    return target

#An arbitrary list of built-in images to choose from.    
images = [Image.ANGRY, Image.ASLEEP, Image.CHESSBOARD, Image.CONFUSED, Image.COW, Image.FABULOUS, Image.GHOST]
image_number = -1

while True:
    #Allows the user to cycle through the preset list of images.
    if button_a.was_pressed():
        image_number = image_number + 1
        if image_number >= len(images):
            image_number = 0
        display.show(images[image_number])
    #Takes the currently displayed image, converts it to a string and broadcasts.
    if button_b.was_pressed():
        message = image_to_string(images[image_number])
        radio.on()
        radio.send(message)
    sleep(50)
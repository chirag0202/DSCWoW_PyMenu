import os
import keyboard, string, random
from playsound import playsound

def keyboardPress(pressedKey):
    """
    function to play sound
    """
    #get list of charaters
    letter = string.ascii_letters

    #get list of digits
    digit = string.digits #gets list of numbers

    #get path of sound
    sound = str("test_sound.mp3")
    if pressedKey in letter or digit:
        playsound(sound)

if __name__ == "__main__":
    keyboardPress('h')
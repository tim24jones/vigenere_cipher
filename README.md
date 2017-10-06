# vigenere_cipher
implementation of the vigenere cipher

A few of the most important functions to be used encoding the vigenere cipher:

A function to select what characters are to be used:
def texttype(mode):
    if mode==all:
        return string.printable
    elif mode==letters:
        return string.ascii_letters
    elif mode==lowercase:
        return string.ascii_lowercase
    elif mode==numbers:
        return string.digits
    else:
        return string.printable

A function to implement a basic caesar cipher given the magnitude of shift(represented by a letter) and an input string to be encoded:
def caesar(input_str,char):
    (will use modular arithmetic to move new letter in string)
    
def vigenere(keyword,input_str):
    (will loop over keyword by calling the caesar function)

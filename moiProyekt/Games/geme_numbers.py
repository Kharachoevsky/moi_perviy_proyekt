
from random import randint

guesses = {}


def number():
    my_number = randint(1, 10)
    guesses['guess'] = my_number
    return guesses

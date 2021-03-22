import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

print(LETTERS)
print(NUMBERS)
print(PUNCTUATION)


class PasswordGenerator():
    def generate(x):
        '''
                Generates a random password having the specified length
                :length -> length of password to be generated. Defaults to 8
                    if nothing is specified.
                :returns string <class 'str'>
                '''
        # create alphanumerical from string constants
        printable = f'{LETTERS}{NUMBERS}'

        # convert printable from string to list and shuffle
        printable = list(printable)
        random.shuffle(printable)

        # generate random password and convert to string
        added_number = random.randrange(1, 9)
        x += added_number
        random_password = random.choices(printable, k=x)
        random_password = ''.join(random_password)
        return random_password

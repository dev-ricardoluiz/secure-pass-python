#from operator import length_hint
import time
import secrets
import string
from random import *

print ('')

for c in range (0, 5): # where '5' is the number of generated passwords
    length_pass = randint(12, 18) # where '12' is the minimum amount of characters and '18' is the maximum amount of characters for each generated password
    char = string.ascii_letters + string.digits + string.punctuation # includes character classes: letters, digits and punctuation
    password = ''.join(secrets.choice(char)for i in range (length_pass)) # here the password is generated
    print(password)
    print('')
    time.sleep(0.5)

print('')
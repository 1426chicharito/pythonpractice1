import string
import random
def generate(a):
    for i in range(0,a):
        letter = random.choice(string.ascii_lowercase)
        print (letter, end='')
a=int(input("Enter:"))
generate(a)

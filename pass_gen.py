import random

def pass_gen(length):
    for x in range(0, length):
        print(random.randrange(0,100))

print("Password length: ")
length = input()

pass_gen(length)
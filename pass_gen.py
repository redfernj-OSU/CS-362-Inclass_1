import random

def pass_gen(length):
    for x in range(1, int(length)):
        print(random.randrange(0,9))

print("Password length: ")
length = input()

pass_gen(length)
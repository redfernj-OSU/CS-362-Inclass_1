import random

def pass_gen(length):
    for x in range(0, int(length)):
        print(random.randrange(0,9), end ="")

print("Password length: ", end="")
length = input()
print()

pass_gen(length)
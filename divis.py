def divisors(num):

    for x in range(num,1, -1):
        if num % x == 0:
            print(num / x)


divisors(10)
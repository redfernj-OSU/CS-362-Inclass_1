def divisors(num):

    for x in range(num,1, -1):
        if num % x == 0:
            print(int(num / x))

    print(num)


divisors(10)
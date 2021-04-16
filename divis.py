def divisors(num):

    print(num)

    for x in range(num,1, -1):
        if num % x == 0:
            print(int(num / x))


divisors(10)
def calc(a, b):

    result = []

    result.append(a + b)
    result.append(a - b)
    result.append(a * b)
    result.append(a / b)

    total = 0

    for x in range(0,3):
        total += result[x]

def count_with_d(n, d):
    data = []
    count = 0
    for i in range(0, n + 1):
        data.append(i ** 2)
    print(data)
    for no in data:
        nos = list(str(no))
        if (str(d) in nos):
            count += 1
    return count

n = int(input('Enter a number: '))
d = int(input('Enter a digit: '))
print(str(count_with_d(n, d)))
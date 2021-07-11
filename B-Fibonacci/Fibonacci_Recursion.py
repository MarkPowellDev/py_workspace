def xFib(n):
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return xFib(n-1) + xFib(n-2)

print(xFib(5))


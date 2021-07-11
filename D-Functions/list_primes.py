

def ifprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range(99):
        if ifprime(n):
            print(n, end=' ', flush=True)
    print()

list_primes()


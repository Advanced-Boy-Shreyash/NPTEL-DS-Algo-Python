fibtable = {}


def fib(n):
    if n in fibtable:
        return (fibtable[n])
    if n == 1 or n == 0:
        value = n
    else:
        value = fib(n-1)+fib(n-2)
    fibtable[n] = value
    return value


print(fib(10))

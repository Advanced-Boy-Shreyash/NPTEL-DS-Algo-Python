# def gcd(m, n):
#     fm = []
#     fn = []
#     cf = []
#     for i in range(1, m+1):
#         if m % i == 0:
#             fm.append(i)
#     for j in range(1, n+1):
#         if n % j == 0:
#             fn.append(j)
#     for f in fm:
#         if f in fn:
#             cf.append(f)
#     return (cf[-1])


# print(gcd(14, 63))

# def gcd(m, n):
#     cf = []
#     for i in range(1, min(m, n)):
#         if m % i == 0 and n % i == 0:
#             cf.append(i)
#     return (max(cf))


# print(gcd(14, 63))


# def gcd(m, n):
#     for i in range(1, min(m, n)+1):
#         if m % i == 0 and n % i == 0:
#             mirf = i
#     return mirf


# print(gcd(14, 63))


# def gcd(m, n):
#     i = min(m, n)
#     while i > 0:
#         if m % i == 0 and n % i == 0:
#             return (i)
#         else:
#             i = i-1


# print(gcd(14, 63))

# Euclid's Algorithm :

# def gcd(m, n):
#     if m < n:
#         m, n = n, m
#         # M=N
#         # N=M
#     if m % n == 0:
#         return (n)
#     else:
#         diff = m-n
#         return (gcd(max(n, diff), min(n, diff)))


# print(gcd(14, 63))


# def gcd(m, n):
#     if m < n:
#         m, n = n, m
#         # M=N
#         # N=M
#     while m % n != 0:
#         diff = m-n
#         m, n = max(n, diff), min(n, diff)
#     return n


# print(gcd(14, 63))


# def gcd(m, n):
#     if m < n:
#         m, n = n, m
#         # M=N
#         # N=M
#     if m % n == 0:
#         return (n)
#     else:
#         diff = m-n
#         return (gcd(n, m % n))


# print(gcd(14, 63))


# def gcd(m, n):
#     if m < n:
#         m, n = n, m
#         # M=N
#         # N=M
#     while m % n != 0:
#         m, n = n, m % n
#     return n


# print(gcd(14, 63))

def factors(n):
    flist = []
    for i in range(1, n+1):
        if n % i == 0:
            flist = flist+[i]
    return (flist)


def isprime(n):
    return (factors(n) == [1, n])

# print(factors(6))
# print(isprime(7))


def uptoprime(n):
    primelist = []
    for i in range(1, n+1):
        if isprime(i):
            primelist = primelist+[i]
    return primelist


# print(uptoprime(9))

def nprime(n):
    '''This function gives first n prime'''
    count, i, plist = 0, 1, []
    while count < n:
        if isprime(i):
            count, plist = count+1, plist+[i]
        i = i+1
    return plist


print(nprime(8))

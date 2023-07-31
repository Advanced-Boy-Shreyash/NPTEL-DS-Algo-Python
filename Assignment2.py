# A positive integer m is a prime product if it can be written as p×q, where p and q are both primes.
# Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise.
# (If m is not positive, your function should return False.)
# Here are some examples of how your function should work.
# >>> primeproduct(6)
# True
# >>> primeproduct(188)
# False
# >>> primeproduct(202)
# True

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primeproduct(m):
    if m < 1:
        return False
    else:
        fact = []
        for i in range(2, m):
            if m % i == 0 and isprime(i):
                fact = fact + [i]

        if len(fact) == 2 and m == fact[0] * fact[1]:
            return True

        if len(fact) == 1 and m == fact[0] * fact[0]:
            return True

        return False


# Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string
# obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s
# Here are some examples to show how your function should work.
# >>> delchar("banana","b")
# 'anana'
# >>> delchar("banana","a")
# 'bnn'
# >>> delchar("banana","n")
# 'baaa'
# >>> delchar("banana","an")
# 'banana'

def delchar(s, c):
    if len(c) == 1:
        s = s.replace(c, '')
        return s
    else:
        return s


# Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first element in l1, then the
# first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the
# remaining elements of the longer list are appended at the end of the shuffled output.
# Here are some examples to show how your function should work.

def shuffle(l1, l2):
    list = []
    maxlen = max(len(l1), len(l2))

    for i in range(maxlen):
        if i < len(l1):
            list.append(l1[i])
        if i < len(l2):
            list.append(l2[i])

    return list


# Test Cases
print(primeproduct(6))
print(primeproduct(188))
print(primeproduct(202))
print(delchar("banana", "b"))
print(delchar("banana", "a"))
print(delchar("banana", "n"))
print(delchar("banana", "an"))
print(shuffle([0, 2, 4], [1, 3, 5]))
print(shuffle([0, 2, 4], [1]))
print(shuffle([0], [1, 3, 5]))

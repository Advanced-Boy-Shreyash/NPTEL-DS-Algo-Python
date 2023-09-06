def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


print(fact(5))


def mul(m, n):
    if n == 1:
        return m
    else:
        return (m+mul(m, n-1))


print(mul(4, 55))


def expanding(l):
    diff = l[1]-l[0]
    for i in range(2, len(l)):
        if diff < abs(l[i]-l[i-1]):
            diff = abs(l[i]-l[i-1])
        else:
            return False
    return True


print(expanding([1, 3, 7, 2, 9]))
print(expanding([1, 3, 7, 2, -3]))


def sumsquare(l):
    odd_squares = []
    even_squares = []

    for i in l:
        squared = i * i
        if i % 2 == 0:
            even_squares.append(squared)
        else:
            odd_squares.append(squared)

    odd_sum = sum(odd_squares)
    even_sum = sum(even_squares)

    return [odd_sum, even_sum]


print(sumsquare([1, 3, 5]))


# def sumsquare(l):
#     even_squares = sum(x ** 2 for x in l if x % 2 == 0)
#     odd_squares = sum(x ** 2 for x in l if x % 2 != 0)
#     return [odd_squares, even_squares]

print(sumsquare([1, 2, 3, 4, 5, 6]))  # Output: [35, 56]


# def transpose(m):
#     l = []
#     for x in zip(*m):
#         transpose_row = list(x)
#         l.append(transpose_row)

#     return l


def transpose(m):
    num_rows = len(m)
    num_cols = len(m[0])
    transposed = []
    for col in range(num_cols):
        transpose_rows = []
        for row in range(num_rows):
            transpose_rows.append(m[row][col])
        transposed.append(transpose_rows)
    return transposed


print(transpose([[1, 2, 3], [4, 5, 6]]))


def QuickSort(A, l, r):
    if r-l <= 1:
        return ()

    yellow = l+1
    for green in range(l+1, r):
        if A[yellow] <= A[l]:
            A[yellow], A[green] = A[green], A[yellow]
            yellow = yellow+1
    A[l], A[yellow-1] = A[yellow-1], A[l]
    QuickSort(A, l, yellow-1)
    QuickSort(A, yellow, r)


l = list(range(500, 0, -1))
print(l, '\n')
QuickSort(l, 0, len(l))
print(l)


def histogram(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    ans = []
    for a in d.keys():
        number_of_times = d[a]
        ans.append((a, number_of_times))
    ans = sorted(ans, key=lambda x: x[0])
    ans = sorted(ans, key=lambda x: x[1])
    return ans

# Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent
# pair of elements strictly increases.

# Here are some examples of how your function should work.

#   >>> expanding([1,3,7,2,9])
#   True
# Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 9-2 = 7.

#   >>> expanding([1,3,7,2,-3])
#   False
# Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 2-(-3) = 5, so not strictly increasing.

#   >>> expanding([1,3,7,10])
#   False

def expanding(l):
    diff = l[1]-l[0]
    for i in range(2, len(l)):
        if abs(l[i]-l[i-1]) > diff:
            diff = abs(l[i]-l[i-1])
        else:
            return False
    return True

# or

# def expanding(l):
#     return all(abs(l[i] - l[i-1]) > abs(l[i-1] - l[i-2]) for i in range(2, len(l)))


print(expanding([1, 3, 7, 2, 9]))
print(expanding([1, 3, 7, 2, -3]))
print(expanding([1, 3, 7, 10]))


# Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares
# all the odd numbers in l and even is the sum of squares of all the even numbers in l.

# Here are some examples to show how your function should work.

# >>> sumsquare([1,3,5])
# [35, 0]

# >>> sumsquare([2,4,6])
# [0, 56]

# >>> sumsquare([-1,-2,3,7])
# [59, 4]

def sumsquare(l):
    temp = []
    temp2 = []

    for i in l:
        squared = i * i
        if i % 2 == 0:
            temp.append(squared)
        else:
            temp2.append(squared)

    f1 = sum(temp)
    f2 = sum(temp2)

    return [f2, f1]

# OR
# def sumsquare(l):
#     even_squares = sum(x ** 2 for x in l if x % 2 == 0)
#     odd_squares = sum(x ** 2 for x in l if x % 2 != 0)
#     return [odd_squares, even_squares]


print(sumsquare([1, 3, 5]))
print(sumsquare([2, 4, 6]))
print(sumsquare([-1, -2, 3, 7]))


# A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.
# For instance, the matrix
# 1  2  3  4
# 5  6  7  8
# would be represented as [[1, 2, 3, 4], [5, 6, 7, 8]].
# The transpose of a matrix converts each row into a column. The transpose of the matrix above is:
# 1  5
# 2  6
# 3  7
# 4  8
# which would be represented as [[1, 5], [2, 6], [3, 7], [4, 8]].
# Write a Python function transpose(m) that takes as input a two dimensional matrix m and returns the transpose of m. The argument m should
# remain undisturbed by the function.
# Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

# >>> transpose([[1,2,3],[4,5,6]])
# [[1, 4], [2, 5], [3, 6]]

# >>> transpose([[1],[2],[3]])
# [[1, 2, 3]]

# >>> transpose([[3]])
# [[3]]

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

# OR
# def transpose(m):
#     l = []
#     for x in zip(*m):
#         transpose_row = list(x)
#         l.append(transpose_row)

#     return l

# OR

# def transpose(m):
#     return [list(x) for x in zip(*m)]


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1], [2], [3]]))
print(transpose([[3]]))

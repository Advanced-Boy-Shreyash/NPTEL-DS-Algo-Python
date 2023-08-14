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
    lise = []
    e, o = 0, 0
    for i in range(0, len(l)):
        if l[i] % 2 == 0:
            e = e + l[i]**2
        else:
            o = o + l[i]**2
    lise.append(o)
    lise.append(e)
    return lise


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
    return [list(x) for x in zip(*m)]


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[1], [2], [3]]))
print(transpose([[3]]))

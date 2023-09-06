def merge(A, B):  # Merge A[0:m],B[0:n]
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)  # Current positions in A,B

    while i+j < m+n:  # i+j is number of elements merged so far

        if i == m:  # Case 1: A is empty
            C.append(B[j])
            j = j+1

        elif j == n:  # Case 2: B is empty
            C.append(A[i])
            i = i+1

        elif A[i] <= B[j]:  # Case 3: Head of A is smaller
            C.append(A[i])
            i = i+1

        elif A[i] > B[j]:  # Case 4: Head of B is smaller
            C.append(B[j])
            j = j+1

    return (C)


# l1 = [54, 32, 87, 65, 21, 7, 96]
# l2 = [4, 78, 45, 8, 98, 541, 22, 54, 5]
# print(merge(l1, l2))

def mergesort(A, left, right):

    if right-left <= 1:
        return (A[right:left])

    if right-left > 1:
        mid = (left+right)//2

        L = mergesort(A, left, mid)
        R = mergesort(A, mid, right)

        return merge(L, R)


l = list(range(0, 100, 2))+list(range(1, 75, 2))
print(l, '\n')
print(mergesort(l, 0, len(l)))

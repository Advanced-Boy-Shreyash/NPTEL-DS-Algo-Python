def merge(l1, l2):
    # temp=[]
    # len_l1=len(l1)
    # len_l2=len(l2)

    temp, len_l1, len_l2 = [], len(l1), len(l2)
    i, j = 0, 0

    while i+j < len_l1+len_l2:

        if i == len_l1:
            temp.append(l2[j])
            j = j+1

        elif j == len_l2:
            temp.append(l1[i])
            i = i+1

        elif l1[i] <= l2[j]:
            temp.append(l1[i])
            i = i+1

        elif l2[j] < l1[i]:
            temp.append(l2[j])
            j = j+1

    return temp


# l1 = [2, 45, 64, 66, 86, 99]
# l2 = [5, 7, 17, 57, 100]
# print(merge(l1, l2))

def mergesort(A, left, right):
    # Sort the slice A[left:right]
    if right - left <= 1:  # Base case
        return (A[left:right])

    if right - left > 1:  # Recursive call
        mid = (left+right)//2

        L = mergesort(A, left, mid)
        R = mergesort(A, mid, right)

        return (merge(L, R))


l = list(range(0, 100, 2))+list(range(1, 75, 2))
print(l, '\n')
print(mergesort(l, 0, len(l)))

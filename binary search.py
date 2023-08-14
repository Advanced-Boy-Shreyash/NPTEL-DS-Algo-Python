# def bsearch(seq, v, l, r):
#     # search for v in seq[l:r], seq is sorted
#     if r - l == 0:
#         return (False)
#     mid = (l + r)  # // 2 // integer division
#     if v == seq[mid]:
#         return (True)
#     if v < seq[mid]:
#         return (bsearch(seq, v, l, mid))
#     else:
#         return (bsearch(seq, v, mid+1, r))


# seq = [3, 54, 5, 26, 45, 65, 56]
# result = bsearch(seq, 2, 0, 7)
# print(result)

pos = -1


def bsearch(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False


list = [4, 7, 8, 12, 45, 99]
n = 45

if bsearch(list, n):
    print("Found n at position", pos+1)

else:
    print("Not Found")

def histogram(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1
    ans = []
    for a in d.keys():
        No_of_a = d[a]
        ans.append((a, No_of_a))
    ans = sorted(ans, key=lambda x: x[0])
    ans = sorted(ans, key=lambda x: x[1])
    return ans


print(histogram([13, 12, 11, 13, 14, 13, 7, 7, 13, 14, 12]))

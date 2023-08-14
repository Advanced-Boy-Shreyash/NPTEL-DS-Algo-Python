def SelectionSort(l):
    for start in range(len(l)):
        minpos = start

        for i in range(start+1, len(l)):
            if l[i] < l[minpos]:
                minpos = i

        l[start], l[minpos] = l[minpos], l[start]


l = [121, 5, 34, 82, 582, 24, 512, 65, 78]
SelectionSort(l)
print(l)

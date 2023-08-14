def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            seq[pos], seq[pos-1] = seq[pos-1], seq[pos]
            pos = pos-1


seq = [454, 65, 2, 658, 523, 645, 255, 45, 64]
InsertionSort(seq)
print(seq)

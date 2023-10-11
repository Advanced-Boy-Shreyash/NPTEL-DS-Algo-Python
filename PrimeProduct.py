def lfds(seq):
    n = len(seq)
    dp = [1]*n

    for i in range(1, n):
        for j in range(i):
            if seq[i] % seq[j] == 0 and dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
    max_length = max(dp)
    print(dp)
    return max_length


l = [
    50,
    2,
    14,
    778,
    916,
    794,
    2,
    14,
    493,
    650,
    422,
    4,
    28,
    691,
    60,
    764,
    4,
    28,
    427,
    173,
    737,
    8,
    56,
    568,
    430,
    783,
    8,
    56,
    124,
    68,
    136,
    16,
    112,
    23,
    59,
    70,
    16,
    112,
    457,
    12,
    43,
    32,
    224,
    422,
    920,
    785,
    32,
    224,
    325,
    316,
    371,
]

res = lfds(l)
print(res)

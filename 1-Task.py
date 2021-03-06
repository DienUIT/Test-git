n = int(input())    #hs
k = int(input())    #de
p = int(input())    #hang
q = int(input())    #vitri

i = 2 * (p - 1) + q

if (i <= k):
    j = i + k
else:
    j = i - k

if (j > n):
    print(-1)
else:
    if (j % 2 == 0):
        print(int(j / 2), 2)
    else:
        print(int(j / 2) + 1, 1)

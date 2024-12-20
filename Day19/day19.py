import heapq

f = open("Day19/day19.txt","r")

a,b = f.read().strip().split('\n\n')
dl = {}

for i in a.split(","):
    i = i.strip()
    dl[i[-1]] = dl.get(i[-1], set()) | {i}

def dp(s):
    arr = [0] * (len(s) + 1)
    arr2 = [0] * (len(s) + 1) 
    arr[0] = arr2[0] = 1
    for i in range(1, len(arr)):
        ptr_chr = s[i-1]
        for p in dl.get(ptr_chr, set()):
            if len(p) <= i and s[i-len(p):i] == p:
                arr2[i] |= arr2[i-len(p)]
                arr[i] += arr[i-len(p)]
    return (arr2[i], arr[i])

out1 = 0
out2 = 0
for i in b.split('\n'):
    a,b = dp(i)
    out1 += a
    out2 += b
print(out1, out2)

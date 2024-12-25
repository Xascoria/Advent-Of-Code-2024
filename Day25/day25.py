f = open("Day25\day25.txt","r")
c = f.read().strip()

l = []
k = []
for i in c.split('\n\n'):
    a = i.split("\n")
    if a[0] == "#" * len(a[0]):
        l += [ tuple(i.count("#") for i in zip(*a)) ]
    else:
        k += [ tuple(i.count("#") for i in zip(*a)) ]
out = 0
for i in range(len(l)):
    for j in range(len(k)):
        arr = [a+b for a,b in zip(l[i], k[j])]
        if max(arr) <= 7:
            out += 1
print(out)
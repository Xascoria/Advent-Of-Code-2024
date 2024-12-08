f = open("Day7\day7.txt", "r")

c = f.read().strip()

final = 0
for i in c.split("\n"):
    a,b=i.split(":")
    a = int(a)
    b = [int(i) for i in b.strip().split()]
    c = {b[0]}

    for j in range(1, len(b)):
        r = set()
        for k in c:
            r |= {k * b[j], k + b[j], int(str(k) + str(b[j]))}
        c = {i for i in r if i <= a}
    if a in c:
        final += a

print(final)


f = open("Day24\day24.txt", "r")
a,b = f.read().split("\n\n")

d = {}

for i in a.split("\n"):
    r,v = i.split(": ")
    d[r] = int(v)


b = b.strip().split("\n")
solved = [False] * len(b)

topologicial_sort = []
t = {}
t2 = {}

while not all(solved):
    for j,i in enumerate(b):
        if solved[j]:
            continue

        left, right = i.split(" -> ")
        operations = left.split()

        if not (operations[0] in d and operations[2] in d):
            continue

        v1 = d[operations[0]]
        v2 = d[operations[2]]
        p = {"AND": v1 & v2, "XOR": v1 ^ v2, "OR": v1 | v2}
        d[right] = p[operations[1]]
        solved[j] = True
f = []

for i in d:
    if i[0] == "z":
        f += [(i, d[i])]
s = "".join([str(i[1]) for i in sorted(f,reverse=1)])
print(int(s, 2))

c = "svm,nbc, z15,kqk,cgq, z23, fnr, z39".split(",")
print(",".join(sorted([i.strip() for i in c])))
# cgq,fnr,kqk,nbc,svm,z15,z23,z15,z23,z39
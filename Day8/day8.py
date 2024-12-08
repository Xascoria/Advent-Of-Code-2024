f = open("Day8\day8.txt", "r")
#f = open("Day8\day8.txt", "r")

c = f.read().strip()

z = {i:[] for i in c if i != "." and i != "\n"}

c = c.split("\n")

for i in range(len(c)):
    for j in range(len(c)):
        if c[i][j] in z:
            z[c[i][j]] = z.get(c[i][j], []) + [(i,j)]

anti_nodes = set()

for v in z:
    u = z[v]
    for i in range(len(u)):
        for j in range(i+1, len(u)):
            a = u[i]
            b = u[j]

            x1, y1 = a
            x2, y2 = b

            p = 2
            while True:
                x3 = p * x1 - (p-1)* x2
                y3 = p * y1 - (p-1)* y2
                if 0 <= x3 < len(c) and 0<=y3<len(c):
                    anti_nodes |= {(x3, y3)}
                else:
                    break
                p += 1

            p = 2
            while True:
                x4 = p * x2 - (p-1) * x1
                y4 = p * y2 - (p-1) * y1
                if 0 <= x4 < len(c) and 0<=y4<len(c):
                    anti_nodes |= {(x4, y4)}
                else:
                    break
                p += 1

nc = [[*i] for i in c]

for i in anti_nodes:
    nc[i[0]][i[1]] = "#"


andition = 0

for i in range(len(c)):
    for j in range(len(c)):
        if c[i][j] != ".":
            if len(z[c[i][j]]) > 1 and (i,j) not in anti_nodes:
                andition += 1

print(len(anti_nodes) + andition)


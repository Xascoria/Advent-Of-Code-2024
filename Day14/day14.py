import math

f = open("Day14\day14.txt")
oc = c = f.read().strip()

WIDE_LENGTH = 101
TALL_LENGTH = 103
m = [[0] * WIDE_LENGTH for _ in range(TALL_LENGTH)]
for i in c.split("\n"):
    a,b=i.split()

    px,py = map(int,a[2:].split(","))
    dx,dy = map(int,b[2:].split(","))
    
    c = ((px + dx * 100)%WIDE_LENGTH, (py + dy * 100)%TALL_LENGTH)
    m[c[1]][c[0]] += 1
quad1 = WIDE_LENGTH//2
quad2 = TALL_LENGTH//2
arr = []
for i in [0, quad1+1]:
    for j in [0, quad2+1]:
        s = 0
        for k in range(quad1):
            for l in range(quad2):
                s += m[j+l][k+i]
        arr += [s]
print(math.prod(arr))
cur_off = 0
while True:
    m = [[0] * WIDE_LENGTH for _ in range(TALL_LENGTH)]
    for i in oc.split("\n"):
        a,b=i.split()

        px,py = map(int,a[2:].split(","))
        dx,dy = map(int,b[2:].split(","))
        
        c = ((px + dx * cur_off)%WIDE_LENGTH, (py + dy * cur_off)%TALL_LENGTH)
        m[c[1]][c[0]] += 1

    image = "\n".join("".join([[" ", "#"][j>0]for j in i])for i in m)
    if "#" * 10 in image:
        print(image)
        print("Cur off:",cur_off)

        if input() == "e":
            break
    cur_off += 1

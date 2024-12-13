import numpy as np

f = open("Day13\day13.txt", "r")
c = f.read().strip()
t = 0
parser = lambda c,s:(int(s.split(c)[1][:-3]), int(s.split(c)[2]))

for i in c.split("\n\n"):
    a,b,prize = i.split("\n")
    ax, ay = parser("+", a)
    bx, by = parser("+", b)
    px, py = parser("=", prize)
    
    A = np.array([[ax, bx], [ay, by]])
    B = np.array([px+10000000000000, py+10000000000000])
    solution = np.linalg.solve(A, B)
    a, b= map(lambda x:int(round(x)),solution)
    if a > 0 and b> 0 and a * ax + b * bx == px+10000000000000 and a* ay + b * by == py+10000000000000:
        t += a * 3 + b
print(t)
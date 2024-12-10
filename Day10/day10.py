f = open("Day10\day10.txt", "r")
c = f.read().strip().split("\n")

def check(i,j):
    stack = [(i,j)] # part 1: {(i,j)}
    pointer = 1

    for k in range(1, len(p)):
        ns = [] # part 1: set()
        for pair in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            for v in stack:
                nx = v[0] + pair[0]
                ny = v[1] + pair[1]
                if 0 <= nx < len(c) and 0 <= ny < len(c):
                    if c[nx][ny] == str(k):
                        ns += [(nx, ny)] # part 1: ns |= {(i,j)}
        stack = ns
        if len(stack) == 0:
            return 0
    return len(stack)
        
out = 0
for i in range(len(c)):
    for j in range(len(c)):
        if c[i][j] == "0":
            out += check(i,j)
print(out)            
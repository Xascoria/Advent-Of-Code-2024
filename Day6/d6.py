f = open("Day6\d6.txt", "r")

c = f.read().strip()

t = c.split("\n")

start_coord = None
for i, j in enumerate(t):
    if "^" in j:
        start_coord = (i, j.index("^"))
        break

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_ind = 0

true_start_coord = start_coord

pd = set()

while True:
    pd.add(start_coord)

    new_coord = (start_coord[0] + dir[dir_ind][0], start_coord[1] + dir[dir_ind][1])

    if new_coord[0] < 0 or new_coord[1] < 0 or new_coord[0] >= len(t) or new_coord[1] >= len(t):
        break

    if t[new_coord[0]][new_coord[1]] == "#":
        dir_ind = (dir_ind+1)%4
    else:
        start_coord = new_coord
print(len(pd))
    
t = [[*i] for i in t]

loop_count = 0

for i in range(len(t)):
    for j in range(len(t)):
        if t[i][j] == "." and (i,j) in pd:
            new_t = t
            new_t[i][j] = "#"

            d = set()
            dir_ind = 0

            start_coord = true_start_coord

            while True:
                if (dir_ind, start_coord) in d:
                    #Loop
                    loop_count += 1
                    break
                d.add((dir_ind, start_coord))

                new_coord = (start_coord[0] + dir[dir_ind][0], start_coord[1] + dir[dir_ind][1])

                if new_coord[0] < 0 or new_coord[1] < 0 or new_coord[0] >= len(t) or new_coord[1] >= len(t):
                    break

                if new_t[new_coord[0]][new_coord[1]] == "#":
                    dir_ind = (dir_ind+1)%4
                else:
                    start_coord = new_coord

            new_t[i][j] = "."

print(loop_count)
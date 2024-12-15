import copy

f = open("Day15/day15.txt")

a,b = f.read().strip().split("\n\n")

m = [[*i] for i in a.split("\n")]
om = copy.deepcopy(m)
b=b.replace("\n","").strip()

def is_in_range(x, y):
    return 0 <= x < len(m) and 0 <= y < len(m)

start_coord = None
for j, i in enumerate(m):
    if "@" in i:
        start_coord = (j, i.index("@"))
        break

direction = {
    "<": (0, -1),
    ">": (0, 1),
    "v": (1, 0),
    "^": (-1, 0),
}
for i in b:
    cur_dir = direction[i]

    nc = (start_coord[0] + cur_dir[0], start_coord[1] + cur_dir[1])
    if not is_in_range(*nc):
        continue
    if m[nc[0]][nc[1]]== "#":
        continue
    if m[nc[0]][nc[1]] == ".":
        m[start_coord[0]][start_coord[1]] = "."
        m[nc[0]][nc[1]] = "@"
        start_coord = nc
        continue

    could_find_blank_space = False
    nx = nc[0]
    ny = nc[1]
    while True:
        nx += cur_dir[0]
        ny += cur_dir[1]
        if m[nx][ny] == ".":
            could_find_blank_space = True
            break
        elif m[nx][ny] == "#":
            break
    
    if could_find_blank_space:
        m[start_coord[0]][start_coord[1]] = "."
        m[nc[0]][nc[1]] = "@"
        m[nx][ny] = "O"
        start_coord = nc

output = 0
for i,j in enumerate(m):
    for k in range(len(j)):
        if m[i][k] == "O":
            output += i * 100 + k
print(output) 

m = om
nm = []
for i in range(len(m)):
    nm += [[]]
    for j in range(len(m)):
        if m[i][j] == "#":
            nm[-1] += ["#", "#"]
        elif m[i][j] == "O":
            nm[-1] += ["[", "]"]
        elif m[i][j] == ".":
            nm[-1] += [".", "."]
        else:
            nm[-1] += ["@", "."]

m = nm
start_coord = None
for j, i in enumerate(m):
    if "@" in i:
        start_coord = (j, i.index("@"))
        break

def allow_push_box(cur_coord, direction):
    nx = cur_coord[0] + direction[0]
    ny = cur_coord[1] + direction[1]
    if m[nx][ny] == "#":
        return (False, set())
    if m[nx][ny] == ".":
        return (True, {cur_coord})
    
    output = set()
    if m[nx][ny] in "[]":
        if m[nx][ny] == "[":
            res1 = allow_push_box( (nx, ny), direction )
            if res1[0]:
                output |= res1[1]
            else:
                return (False, set())
            res2 = allow_push_box( (nx, ny+1), direction )
            if res2[0]:
                output |= res2[1]
            else:
                return (False, set())
        else:
            res1 = allow_push_box( (nx, ny), direction )
            if res1[0]:
                output |= res1[1]
            else:
                return (False, set())
            res2 = allow_push_box( (nx, ny-1), direction )
            if res2[0]:
                output |= res2[1]
            else:
                return (False, set())
    return (True, output | {cur_coord})

for i in b:
    cur_dir = direction[i]
    nc = (start_coord[0] + cur_dir[0], start_coord[1] + cur_dir[1])
    if m[nc[0]][nc[1]]== "#":
        continue
    if m[nc[0]][nc[1]] == ".":
        m[start_coord[0]][start_coord[1]] = "."
        m[nc[0]][nc[1]] = "@"
        start_coord = nc
        continue
    
    if i == ">" or i == "<":
        could_find_blank_space = False
        nx = nc[0]
        ny = nc[1]
        while True:
            nx += cur_dir[0]
            ny += cur_dir[1]
            if m[nx][ny] == ".":
                could_find_blank_space = True
                break
            elif m[nx][ny] == "#":
                break
        
        if could_find_blank_space:
            ydiff = -cur_dir[1]

            for i in range(ny, start_coord[1], ydiff):
                m[nx][i] = m[nx][i+ydiff]
            
            m[start_coord[0]][start_coord[1]] = "."
            m[nc[0]][nc[1]] = "@"

            start_coord = nc
    else:
        res1 = allow_push_box(nc, cur_dir)
        if not res1[0]:
            continue
        if m[nc[0]][nc[1]] == "[":
            res2 = allow_push_box((nc[0], nc[1] + 1), cur_dir)
        elif m[nc[0]][nc[1]] == "]":
            res2 = allow_push_box((nc[0], nc[1] - 1), cur_dir)
        if not res2[0]:
            continue
        all_affected_coords = res1[1] | res2[1]

        d = {i[0]: [] for i in all_affected_coords}
        for e in all_affected_coords:
            d[e[0]] += [e]
        ordered_by_rows = [*d.values()]
        ordered_by_rows.sort(key=lambda x:x[0][0], reverse=cur_dir==(1, 0))
        
        for i in ordered_by_rows:
            for j in i:
                nx = j[0] + cur_dir[0]
                ny = j[1] + cur_dir[1]
                m[nx][ny] = m[j[0]][j[1]]
                m[j[0]][j[1]] = "."
        m[start_coord[0]][start_coord[1]] = "."
        m[nc[0]][nc[1]] = "@"
        start_coord = nc

output = 0
for i,j in enumerate(m):
    for k in range(len(j)):
        if m[i][k] == "[":
            output += i * 100 + k
print(output) 
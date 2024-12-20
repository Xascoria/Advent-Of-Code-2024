import heapq

f = open("Day20/day20.txt", "r")
c = f.read().strip().split('\n')

start_coord = None
end_coord = None

directions = [(0, 1), (1,0),(0, -1), (-1, 0)]

for j, i in enumerate(c):
    for k in range(len(i)):
        if i[k] == "S":
            start_coord = (j, k)
        elif i[k] == "E":
            end_coord = (j, k)

def is_in_range(x, y):
    return 0 <= x < len(c) and 0 <= y < len(c)

def bfs(start_coord, matrix):
    matrix[start_coord[0]][start_coord[1]] = 0
    priority_queue = [(0, start_coord)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if matrix[current_node[0]][current_node[1]] < current_distance:
            continue
        
        for d in directions:
            nx = d[0] + current_node[0]
            ny = d[1] + current_node[1]
            if is_in_range(nx, ny) and c[nx][ny] != "#" and current_distance + 1 < matrix[nx][ny]:
                matrix[nx][ny] = current_distance + 1
                heapq.heappush( priority_queue, (current_distance + 1, (nx, ny)) )

bfs_start_matrix = [[float("inf")]  * len(c) for _ in range(len(c))]
bfs_end_matrix = [[float("inf")]  * len(c) for _ in range(len(c))]

bfs(start_coord, bfs_start_matrix)
bfs(end_coord, bfs_end_matrix)

shortest = bfs_start_matrix[end_coord[0]][end_coord[1]]

relative_coords_to_check = set()
CHEAT_TIME = 20
for i in range(-CHEAT_TIME, CHEAT_TIME+1):
    for j in range(-CHEAT_TIME, CHEAT_TIME+1):
        if i == j == 0:
            continue
        if abs(i) + abs(j) <= CHEAT_TIME:
            relative_coords_to_check.add( (i,j) )

out = 0
for i in range(len(c)):
    for j in range(len(c)):
        if c[i][j] != "#":
            sv = bfs_start_matrix[i][j]
            for m in relative_coords_to_check:
                nx = i + m[0]
                ny = j + m[1]
                if is_in_range(nx, ny) and c[nx][ny] != "#":
                    ev = bfs_end_matrix[nx][ny]
                    if sv + ev + abs(m[0]) + abs(m[1]) + 100<= shortest:
                        out += 1

print(out)

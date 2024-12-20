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

def dijkstra(cheat_set = set()):
    shortest_dist = {}
    shortest_dist[start_coord] = 0

    priority_queue = [(0, start_coord)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        for d in directions:
            nx = d[0] + current_node[0]
            ny = d[1] + current_node[1]
            if is_in_range(nx, ny) and (c[nx][ny] != "#" or (nx, ny) in cheat_set):
                if current_distance + 1 < shortest_dist.get((nx, ny), float("inf")):
                    shortest_dist[(nx, ny)] = current_distance + 1
                    heapq.heappush( priority_queue, ( current_distance + 1, (nx, ny) ) )
        
        if end_coord in shortest_dist:
            break
    return shortest_dist[end_coord]

shortest = dijkstra()

off_dir = [(0, 1), (1,0)]
out = 0
concern_set = {}
for i in range(len(c)):
    for j in range(len(c)):
        if c[i][j] == "#":
            p = dijkstra( {(i, j)} )
            if p + 100 <=  shortest:
                out += 1
                saved_time = shortest - p
                #concern_set[saved_time] = concern_set.get(saved_time, set()) | {(i,j)}
    print("Progress:",i)

print(shortest)
print(out)
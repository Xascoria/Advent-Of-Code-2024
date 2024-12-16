import heapq

f = open("Day16\day16.txt", "r")

c = f.read().strip().split("\n")

end_coord = None
start_coord = None

shortest_dist = {}
prev_node = {}
directions = [(0, 1), (1,0),(0, -1), (-1, 0)]

for j,i in enumerate(c):
    if "E" in i:
        end_coord = (j, i.index("E"))
    if "S" in i:
        start_coord = (j, i.index("S"))
    for k in range(len(i)):
        if i[k] != "#":
            shortest_dist[ (j, k) ] = {}
            prev_node[(j, k)] = {}
            for d in directions:
                shortest_dist[ (j, k) ][d] = float("inf")
                prev_node[((j, k), d)] = set()

shortest_dist[ start_coord][(0,1)] = 0
priority_queue = [(0, (start_coord, (0,1)))]

while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)
    cur_coord, cur_dir = current_node

    if current_distance > shortest_dist[cur_coord][cur_dir]:
        continue

    cur_dir_index = directions.index(cur_dir)

    oppo_dir_index = (cur_dir_index + 2)%4
    left_index, right_index = (cur_dir_index - 1)%4, (cur_dir_index + 1)%4

    if current_distance + 1000 <= shortest_dist[cur_coord][directions[left_index]]:
        if current_distance + 1000 == shortest_dist[cur_coord][directions[left_index]]:
            prev_node[(cur_coord,directions[left_index])] |= {current_node}
        else:
            prev_node[(cur_coord,directions[left_index])] = {current_node}
            heapq.heappush(priority_queue, (current_distance + 1000, (cur_coord,directions[left_index])))
        shortest_dist[cur_coord][directions[left_index]] = current_distance + 1000
    if current_distance + 1000 <= shortest_dist[cur_coord][directions[right_index]]:
        if current_distance + 1000 == shortest_dist[cur_coord][directions[right_index]]:
            prev_node[(cur_coord,directions[right_index])] |= {current_node}
        else:
            prev_node[(cur_coord,directions[right_index])] = {current_node}
            heapq.heappush(priority_queue, (current_distance + 1000, (cur_coord,directions[right_index])))
        shortest_dist[cur_coord][directions[right_index]] = current_distance + 1000
        
    if current_distance + 2000 <= shortest_dist[cur_coord][directions[oppo_dir_index]]:
        if current_distance + 2000 == shortest_dist[cur_coord][directions[oppo_dir_index]]:
            prev_node[(cur_coord,directions[oppo_dir_index])] |= {current_node}
        else:
            prev_node[(cur_coord,directions[oppo_dir_index])] = {current_node}
            heapq.heappush(priority_queue, (current_distance + 2000, (cur_coord,directions[oppo_dir_index])))
        shortest_dist[cur_coord][directions[oppo_dir_index]] = current_distance + 2000
    if c[cur_coord[0] + cur_dir[0]][cur_coord[1] + cur_dir[1]] != "#":
        nc = (cur_coord[0] + cur_dir[0], cur_coord[1] + cur_dir[1])
        if current_distance + 1 <= shortest_dist[nc][cur_dir]:
            if current_distance + 1 == shortest_dist[nc][cur_dir]:
                prev_node[(nc,cur_dir)] |= {current_node}
            else:
                prev_node[(nc,cur_dir)] = {current_node}
                heapq.heappush(priority_queue, (current_distance + 1, (nc, cur_dir)))
            shortest_dist[nc][cur_dir] = current_distance + 1

res = min([ shortest_dist[end_coord][i] for i in shortest_dist[end_coord]])
print(res)

visited_set = { end_coord }
cur_stack = { (end_coord,i) for i in shortest_dist[end_coord] if shortest_dist[end_coord][i] == res}

while cur_stack:
    ns = set()
    for i in cur_stack:
        visited_set.add(i[0])
        ns |= prev_node[i]
    cur_stack = ns
print(len(visited_set))
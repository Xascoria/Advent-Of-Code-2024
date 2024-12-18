import heapq

f = open("Day18\day18.txt", "r")
c = f.read().strip().split("\n")

corrupted = []
for j,i in enumerate(c):
    a,b = map(int,i.split(","))
    corrupted.append((a,b))

directions = [(0, 1), (1,0),(0, -1), (-1, 0)]
def run_dij(iteration):
    corrupted_set = set(corrupted[:iteration])

    shortest_dist = {}
    shortest_dist[(0,0)] = 0

    priority_queue = [(0, (0,0))]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_dist[current_node]:
            continue

        for d in directions:
            nx = d[0] + current_node[0]
            ny = d[1] + current_node[1]
            if 0 <= nx <= 70 and 0 <= ny <= 70 and (nx, ny) not in corrupted_set:
                if current_distance + 1 < shortest_dist.get((nx, ny), float("inf")):
                    shortest_dist[(nx, ny)] = current_distance + 1
                    heapq.heappush( priority_queue, ( current_distance + 1, (nx, ny) ) )
        if (70, 70) in shortest_dist:
            break
    return ((70, 70) in shortest_dist, shortest_dist.get((70,70), -1))

print(run_dij(1024))
for i in range(1025, len(corrupted)):
    a,b = run_dij(i)
    if not a:
        print(i,corrupted[i-1])
        break
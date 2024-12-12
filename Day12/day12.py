f = open("Day12\day12.txt", "r")

c = f.read().strip().split("\n")
c = [[*i] for i in c]

m = [[False]*len(c) for _ in range(len(c))]
final = 0
final2 = 0

def calculate_edges(coord_set):
    edges_set = {}
    for s in coord_set:
        for enindex, pair in enumerate([(0,1),(0,-1),(1,0), (-1, 0)]): # y - row
            nx = pair[0] + s[0]
            ny = pair[1] + s[1]
            if (nx, ny) not in coord_set:
                if (nx, ny) not in edges_set:
                    edges_set[(nx, ny)] = [-1,-1,-1,-1]
                edges_set[(nx, ny)][enindex] = 0

    final = 0
    moveable_side = [[(1,0), (-1, 0)], [(1,0), (-1, 0)], [(0,1),(0,-1)], [(0,1),(0,-1)]]

    for i in edges_set:
        for jindex, j in enumerate(edges_set[i]):
            if j == 0:
                unprocessed = {i}
                while len(unprocessed) > 0:
                    nunp = set()
                    for unp in unprocessed:
                        edges_set[unp][jindex] = 1
                        for pair in moveable_side[jindex]:
                            nx = pair[0] + unp[0]
                            ny = pair[1] + unp[1]
                            if (nx, ny) in edges_set and edges_set[(nx, ny)][jindex] == 0:
                                nunp.add((nx, ny))
                    unprocessed = nunp
                final += 1

    return final
    

for i in range(len(c)):
    for j in range(len(c)):
        if m[i][j] == False:
            considered = set()
            stack = {(i,j)}

            current_char = c[i][j]

            while len(stack) > 0:
                ns = set()
                
                for s in stack:
                    for pair in [(0,1),(1,0),(0,-1),(-1,0)]:
                        nx = pair[0] + s[0]
                        ny = pair[1] + s[1]

                        if 0<=nx < len(c) and 0<=ny < len(c) and c[nx][ny] == current_char and (nx, ny) not in considered and (nx, ny) not in stack:
                            ns.add( (nx, ny) )
                considered |= stack
                stack = ns

            edge_count = calculate_edges(considered)
            area = 0
            perimeter = 0
            for con in considered:
                area += 1
                for pair in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx = pair[0] + con[0]
                    ny = pair[1] + con[1]
                    if (nx, ny) not in considered:
                        perimeter += 1
            final += area*perimeter
            final2 += area * edge_count
        
        for p in considered:
            m[p[0]][p[1]] = True

print(final)
print(final2)

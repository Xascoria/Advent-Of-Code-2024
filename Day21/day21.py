import functools

c = """140A
169A
170A
528A
340A"""

og_keypad = ["789", "456", "123", " 0A"]
og_position = (3, 2)

directional_keypad = [" ^A","<v>"]
dir_start_pos = (0, 2)

def find_coord(m, c):
    for i in range(len(m)):
        if c in m[i]:
            return (i, m[i].index(c))
    raise Exception("no" + str(m) + " " + c)

search_dict = {}
y = "".join(directional_keypad).strip()

for i in range(len(y)):
    search_dict[y[i]] = {}
    for j in range(len(y)):
        if i == j:
            search_dict[y[i]][y[j]] = ["A"]
            continue
        a = find_coord(directional_keypad, y[i])
        b = find_coord(directional_keypad, y[j])

        search_dict[y[i]][y[j]] = []
        coord_dist = (b[0]- a[0],b[1] - a[1])
        updown = "^v"[coord_dist[0] > 0]
        leftright = "<>"[coord_dist[1] > 0]
        arr = updown * abs(coord_dist[0]) + leftright * abs(coord_dist[1])
        if len(set(arr)) == 1:
            search_dict[y[i]][y[j]] = [arr + "A"]
        else:
            if directional_keypad[a[0] + coord_dist[0]][a[1]] != " ":
                search_dict[y[i]][y[j]] += [arr + "A"]
            if directional_keypad[a[0]][a[1] + coord_dist[1]] != " ":
                search_dict[y[i]][y[j]] += [arr[::-1] + "A"]

@functools.cache
def get_final_length(s, start_coord, layer=1):
    if layer == 26:
        return len(s)
    final_length = 0
    for i in range(len(s)):
        pos_path = search_dict[directional_keypad[start_coord[0]][start_coord[1]]][s[i]]
        final_length += min([get_final_length(p, dir_start_pos, layer+1) for p in pos_path])
        start_coord = find_coord(directional_keypad, s[i])
    return final_length

final = 0
for i in c.split("\n"):
    start_coord = og_position
    b = 0

    for j in range(len(i)):
        target_coord = find_coord(og_keypad, i[j])
        nx = target_coord[0] - start_coord[0]
        ny = target_coord[1] - start_coord[1]
        updown = "^v"[nx > 0]
        leftright = "<>"[ny > 0]
        potential_path = updown * abs(nx) + leftright * abs(ny)
        if len(set(potential_path)) == 1:
            b += get_final_length(potential_path + 'A', dir_start_pos, 1)
        elif og_keypad[start_coord[0] + nx][start_coord[1]] == " ":
            b += get_final_length(potential_path[::-1] + 'A', dir_start_pos, 1)
        elif og_keypad[start_coord[0]][start_coord[1] + ny] == " ":
            b += get_final_length(potential_path + 'A', dir_start_pos, 1)
        else:
            r1 = get_final_length(potential_path + 'A', dir_start_pos, 1)
            r2 = get_final_length(potential_path[::-1] + 'A', dir_start_pos, 1)
            b += min(r1, r2)
        start_coord = target_coord
    final += b * int(i[:-1])
print(final)
import itertools

f = open("Day23/day23.txt", "r")
c = f.read().strip()
connect = {}

for i in c.split("\n"):
    a,b = i.split("-")
    connect[a] = connect.get(a, set()) | {b}
    connect[b] = connect.get(b, set()) | {a}

arr = [*connect]
p = set()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] in connect[arr[i]]:
            cross = connect[arr[i]] & connect[arr[j]]
            for c in cross:
                p.add( (*sorted([c, arr[i],arr[j]]),) )
c = 0
for i in p:
    for j in i:
        if j[0] == "t":
            c += 1
            break
print(c)

max_set = []
for i in range(len(arr)):
    
    for j in range(1, len( connect[arr[i]] )+1):
        combis = itertools.combinations(connect[arr[i]], j)
        for c in combis:
            starting_set = list({ arr[i] } | {*c })
            if len(starting_set) < len(max_set):
                continue
            is_connected = True
            for aa in range(len(starting_set)):
                for bb in range(aa+1, len(starting_set)):
                    if starting_set[aa] not in connect[starting_set[bb]]:
                        is_connected = False
                        break
                if not is_connected:
                    break
            if is_connected and len(starting_set) > len(max_set):
                max_set = starting_set
print(*sorted(max_set),sep=',')
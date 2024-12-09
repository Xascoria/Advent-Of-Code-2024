import copy

f = open("Day9\day9.txt", "r")

c = f.read().strip()

memory = []

last_memory = -1
first_slot = -1

for j, i in enumerate(c):
    if j % 2 == 0:
        memory.append( (j//2, int(i)) )
        last_memory = j
    else:
        memory.append( [(-1, int(i))] )
        if first_slot == -1: first_slot = j

og_lm = last_memory
og_fs = first_slot
og_memory = copy.deepcopy(memory)


while first_slot < last_memory:
    a = memory[first_slot][-1][1]
    b = memory[last_memory][1]


    if a == 0:
        first_slot += 2
    elif a > b:
        memory[first_slot] = memory[first_slot][:-1] + [ (memory[last_memory][0], b), (-1, a-b) ]
        memory[last_memory] = (-1, 0)
        last_memory -= 2
    elif a < b:
        memory[first_slot] = memory[first_slot][:-1] + [ (memory[last_memory][0], a) ]
        first_slot += 2
        memory[last_memory] = (memory[last_memory][0], b-a)
    else:
        memory[first_slot] = memory[first_slot][:-1] + [ (memory[last_memory][0], a) ]
        memory[last_memory] = (-1, 0)
        first_slot += 2
        last_memory -= 2

final = []
for i in range(len(memory)):
    if i % 2 == 0:
        final += [memory[i][0]] * memory[i][1]
    else:
        for j in memory[i]:
            final += [j[0]] * j[1]

cs = 0
for i in range(len(final)):
    if final[i] > -1:
        cs += i * final[i]
print(cs)

last_memory = og_lm 
memory = og_memory 

for i in range(last_memory, -1, -2):
    for j in range(1, i, 2):
        a = memory[j][-1][1]
        b = memory[i][1]

        if memory[j][-1][0] != -1:
            continue
        elif a >= b:
            if a > b:
                memory[j] = memory[j][:-1] + [ (memory[i][0], b), (-1, a-b) ]
                memory[i] = (-1, b)
                break
            elif a == b:
                memory[j] = memory[j][:-1] + [ (memory[i][0], a) ]
                memory[i] = (-1, b)
                break

final = []
for i in range(len(memory)):
    if i % 2 == 0:
        final += [memory[i][0]] * memory[i][1]
    else:
        for j in memory[i]:
            final += [j[0]] * j[1]
   
cs = 0
for i in range(len(final)):
    if final[i] > -1:
        cs += i * final[i]
print(cs)
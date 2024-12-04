f = open("Day1\d1.txt", "r")

c = f.read().strip().split("\n")

a = []
b = []
for i in c:
    n1, n2 = map(int, i.split())
    a += [n1]
    b += [n2]

a.sort()
b.sort()

diff = 0

for i in zip(a, b):
    diff += abs(i[0]-i[1])

print(diff)

freq_dict = {}

for i in b:
    freq_dict[i] = freq_dict.get(i,0)+1

sim = 0
for i in a:
    sim += i * freq_dict.get(i, 0)
print(sim)
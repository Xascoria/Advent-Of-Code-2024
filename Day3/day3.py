import re

f = open("Day3\day3.txt", "r")

c = f.read()


pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, c)

t = 0
for i in matches:
    t += int(i[0]) *int(i[1])
print(t)

pattern = r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)"
new_matches = re.findall(pattern, c)

enabled = True

t = 0
for i in new_matches:
    if i == "don't()":
        enabled = False
    elif i == "do()":
        enabled = True
    else:
        if enabled:
            a,b = i.split(",")
            b = int(b[:-1])
            a = int(a.split("(")[1])
            t += a*b
print(t)
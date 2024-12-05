f = open("Day5\day5.txt", "r")

con = f.read().strip()

a,b = con.split("\n\n")

rules = {}

for i in a.strip().split():
    d,f = map(int,i.split("|"))
    rules[d] = rules.get(d,set()) | {f}

mid = 0
umid = 0

for i in b.strip().split():
    t = [*map(int,i.split(","))]

    Falty = False
    for j in range(len(t)):
        for k in range(j+1, len(t)):
            if t[j] not in rules or t[k] not in rules[t[j]]:
                Falty = True
                break

        if Falty:
            break
    
    if not Falty:
        mid += t[len(t)//2]
    else:
        #part 2
        for j in range(len(t)):
            for k in range(j+1, len(t)):
                if t[j] not in rules or t[k] not in rules[t[j]]:
                    t[j],t[k] = t[k],t[j]
        umid += t[len(t)//2]
            

print(mid)
print(umid)


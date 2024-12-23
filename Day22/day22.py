f = open("Day22\day22.txt", "r")
c = f.read().strip().split("\n")

def ss(n):
    n ^= (n * 64) 
    n = n % 16777216
    n ^= int(n / 32)
    n = n % 16777216
    n ^= n*2048
    n = n % 16777216
    return n

sequence_tree = {}
final = 0
for j,i in enumerate(c):
    i = int(i)

    changes = [i%10]
    abs_prices = [i%10]
    for _ in range(2000):
        i = ss(i)
        changes += [i%10 - abs_prices[-1]]
        abs_prices += [i%10]

    for k in range(1, len(abs_prices) - 4):
        s = (*changes[k:k+4],)
        if s not in sequence_tree:
            sequence_tree[s] = {}
        if j not in sequence_tree[s]:
            sequence_tree[s][j] = abs_prices[k+3]
    final += i

print(final)
print(max([sum(sequence_tree[i].values()) for i in sequence_tree]))
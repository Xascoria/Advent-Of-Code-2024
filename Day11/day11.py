s = [*map(int,"5910927 0 1 47 261223 94788 545 7771".split())]

for i in range(25):
    ns = []
    for j in range(len(s)):
        if s[j] == 0:
            ns += [1]
        elif len(str(s[j]))%2==0:
            p = len(str(s[j]))//2
            ns += [ int(str(s[j])[:p]), int(str(s[j])[p:]) ]
        else:
            ns += [s[j]*2024]
    s = ns
    print("i:",i)
print(len(s))
s = [*map(int,"5910927 0 1 47 261223 94788 545 7771".split())]

map_dict = {0:(1,)}
rec_dict = {}

def recursion(cal_t, layer=0):
    if cal_t in rec_dict:
        if rec_dict[cal_t] <= layer:
            return
    rec_dict[cal_t] = layer

    if layer == 76:
        return

    if cal_t in map_dict:
        for i in map_dict[cal_t]:
            recursion(i, layer+1)
        return
    
    if len(str(cal_t))%2==0:
        p = len(str(cal_t))//2
        map_dict[cal_t] = (int(str(cal_t)[:p]), int(str(cal_t)[p:]))
    else:
        map_dict[cal_t] = (2024*cal_t,)
    
    for i in map_dict[cal_t]:
        recursion(i, layer+1)

rar = {}
def rec_2(num, layer=0):
    if layer == 75:
        return 1
    
    out = 0
    for i in map_dict[num]:
        if (i, layer+1) in rar:
            out += rar[(i, layer+1)]
        else:
            fig = rec_2(i, layer+1)
            rar[(i, layer+1)] = fig
            out += fig
    return out
    
out = 0
for i in s:
    recursion(i, 0)
for i in s:
    out += rec_2(i, 0)
print(out)
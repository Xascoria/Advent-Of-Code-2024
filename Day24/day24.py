

f = open("Day24\day24.txt", "r")
a,b = f.read().split("\n\n")

d = {}

for i in a.split("\n"):
    r,v = i.split(": ")
    d[r] = int(v)


b = b.strip().split("\n")
solved = [False] * len(b)

topologicial_sort = []
t = {}

while not all(solved):
    for j,i in enumerate(b):
        if solved[j]:
            continue

        left, right = i.split(" -> ")
        operations = left.split()

        if not (operations[0] in d and operations[2] in d):
            continue

        v1 = d[operations[0]]
        v2 = d[operations[2]]
        p = {"AND": v1 & v2, "XOR": v1 ^ v2, "OR": v1 | v2}
        d[right] = p[operations[1]]
        t[right] = (operations[1], *sorted([operations[0], operations[2]]), right)
        solved[j] = True
f = []

for i in d:
    if i[0] == "z":
        f += [(i, d[i])]
s = "".join([str(i[1]) for i in sorted(f,reverse=1)])
print(int(s, 2))

def check_register(count, tree):
    if (count == 45 and tree[0] != 'OR') or (count < 45 and tree[0] != 'XOR'):
        print("Err1: ", count, tree)
    else:
        a = tree[1]
        b = tree[2]
        if a in t and b in t:
            s = sorted([t[a], t[b]])
            if count > 1 and s[0][0] != "OR" and [*s[1][:-1]] != ["XOR","x"+int_to_zreg(count)[1:], "y"+int_to_zreg(count)[1:]]:
                print("Err2: ", count, s)
            else:
                if s[0][1] in t and s[0][2] in t:
                    ora = t[s[0][1]]
                    orb = t[s[0][2]]
                    ss = sorted([ora, orb])
                    if ss[0][0] != "AND" or ss[1][0] != "AND" or ss[1][1][0] != "x":
                        print("Err5: ", count, ss)
                    else:
                        check_carry_on(ss[0], count)
                else:
                    print("Err3", count, s)

def check_carry_on(root, layer):
    if layer == 1:
        if [*root][:3] != ['AND','x1','y1']:
            print("Err5: ", layer, root)
        return
    
    ora = t[root[1]]
    orb = t[root[2]]
    ss = sorted([ora, orb])
    if ss[0][0] != "AND" or ss[1][0] != "AND" or ss[1][1][0] != "x":
        if ss[0][0] != "OR" or ss[1][0] != "XOR" or ss[1][1][0] != "x":
            print("Err8: ", layer, root, ss)
    try:
        check_carry_on(ss[0], layer-1)
    except:
        print("Err9: ",root, layer)
    
def int_to_zreg(n):
    return "z" + str(n).zfill(2)

for i in sorted(f):
    n = int(i[0][1:])
    if n >= 1:
        check_register(n, t[i[0]])

# Err8:  2 ('AND', 'dqq', 'wbd', 'kwk') [('AND', 'x00', 'y00', 'wbd'), ('XOR', 'x01', 'y01', 'dqq')]
# Err5:  1 ('AND', 'x00', 'y00', 'wbd')
# Err5:  1 ('AND', 'dqq', 'wbd', 'kwk')
# Err5:  1 ('OR', 'kwk', 'mhb', 'vnc')
# Err2:  5 [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
# Err5:  6 [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
# Err8:  6 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
# Err8:  5 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
# Err9:  ('AND', 'rgq', 'svm', 'skn') 5
# Err8:  5 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
# Err8:  4 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
# Err9:  ('AND', 'rgq', 'svm', 'skn') 4
# Err8:  4 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
# Err8:  3 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
# Err9:  ('AND', 'rgq', 'svm', 'skn') 3
# Err8:  3 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
# Err8:  2 ('AND', 'rgq', 'svm', 'skn') [('AND', 'x05', 'y05', 'svm'), ('OR', 'brg', 'ppw', 'rgq')]
# Err5:  1 ('AND', 'x05', 'y05', 'svm')
# Err8:  2 ('OR', 'nbc', 'skn', 'pdf') [('AND', 'rgq', 'svm', 'skn'), ('XOR', 'x05', 'y05', 'nbc')]
# Err5:  1 ('AND', 'rgq', 'svm', 'skn')
# Err5:  1 ('OR', 'nbc', 'skn', 'pdf')
# Err5:  1 ('AND', 'pdf', 'wcw', 'fcv')
# Err5:  1 ('OR', 'fcv', 'kwc', 'cqp')
# Err1:  15 ('OR', 'dkk', 'pbd', 'z15')
# Err5:  16 [('OR', 'wfh', 'wth', 'cpv'), ('XOR', 'x15', 'y15', 'fwr')]
# Err8:  17 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'hdk', 'rhs', 'npf')
# Err8:  16 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('AND', 'ktj', 'npf', 'hdf')
# Err8:  15 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'hdf', 'vjc', 'jfn')
# Err8:  14 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('AND', 'fmc', 'jfn', 'tjk')
# Err8:  13 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'pdh', 'tjk', 'vws')
# Err8:  12 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('AND', 'tbk', 'vws', 'wvf')
# Err8:  9 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'fpb', 'rpr', 'kjr')
# Err8:  8 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('AND', 'dnq', 'kjr', 'qnv')
# Err8:  7 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'kkq', 'qnv', 'ckr')
# Err8:  6 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('AND', 'ckr', 'ttw', 'phn')
# Err8:  5 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'dhr', 'phn', 'tdb')
# Err8:  4 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('AND', 'mdg', 'tdb', 'wth')
# Err8:  3 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('OR', 'wfh', 'wth', 'cpv')
# Err8:  2 ('AND', 'kqk', 'rbr', 'bbm') [('XOR', 'cpv', 'fwr', 'kqk'), ('XOR', 'x16', 'y16', 'rbr')]
# Err5:  1 ('XOR', 'cpv', 'fwr', 'kqk')
# Err5:  1 ('AND', 'kqk', 'rbr', 'bbm')
# Err5:  1 ('OR', 'bbm', 'qbc', 'gcc')
# Err5:  1 ('AND', 'dhd', 'gcc', 'bdv')
# Err5:  1 ('OR', 'bdv', 'grk', 'dbd')
# Err5:  1 ('AND', 'dbd', 'tcb', 'fwn')
# Err5:  1 ('OR', 'djp', 'fwn', 'bbc')
# Err1:  39 ('AND', 'bdr', 'fsp', 'z39')
# Err5:  40 [('AND', 'x39', 'y39', 'nrj'), ('XOR', 'bdr', 'fsp', 'fnr')]

# sbn
# z23, cgq
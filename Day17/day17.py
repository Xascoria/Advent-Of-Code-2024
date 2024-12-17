s = """Register A: 22817223
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0"""

# s = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0"""

a,b = s.split("\n\n")
t = a.split("\n")

areg = int(t[0].split(": ")[1])
breg = int(t[1].split(": ")[1])
creg = int(t[2].split(": ")[1])

prog = [*map(int,b.split(": ")[1].split(","))]

def run_program(areg, breg, creg):
    cur_ptr = 0
    s = ''
    while cur_ptr < len(prog):
        opcode = prog[cur_ptr]
        operand = prog[cur_ptr+1]

        combovaluemap = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: areg,
            5: breg,
            6: creg,
            7: "What"
        }
        combovalue = combovaluemap[operand]

        if opcode == 0:
            na = areg // (2**combovalue)
            areg = na
        elif opcode == 1:
            breg = breg ^ operand
        elif opcode == 2:
            breg = combovalue % 8
        elif opcode == 3:
            if areg != 0:
                cur_ptr = operand * 2
                continue
        elif opcode == 4:
            breg = breg ^ creg
        elif opcode == 5:
            s += str(combovalue%8) + ","
        elif opcode == 6:
            na = areg // (2**combovalue)
            breg = na
        elif opcode == 7:
            na = areg // (2**combovalue)
            creg = na
        cur_ptr += 2
    return s[:-1]

print(run_program(areg, breg, creg))
rp = prog[::-1]
def reverse_engi(ptr = 0, pos_a_remain = 0):
    if ptr == len(rp):
        return pos_a_remain // 8

    output = float("inf")
    for i in range(8):
        pos_a = pos_a_remain + i
        res = run_program(pos_a, breg, creg)
        
        parsed_res = [*map(int,res.split(","))][::-1]
        if parsed_res == rp[:len(parsed_res)]:
            output = min(output, reverse_engi(ptr+1, pos_a * 8))
    return output
print( reverse_engi() )


f = open("Day4\day4.txt", "r+")

c = f.read().strip().split("\n")

length = len(c)

pp = []


def eight_direc_search(i, j):
    global pp
    arr = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1,1)]

    t = " MAS"
    count = 0

    for pair in arr:
        not_equal = False
        out_of_range = False
        for index in range(1, 4):
            cell_x = i + pair[0] * index
            cell_y = j + pair[1] * index

            try:
                if cell_x < 0 or cell_y < 0:
                    raise Exception("p")

                p = c[cell_x][cell_y] == t[index]
                if not p:
                    not_equal = True
                    break
            except:
                out_of_range = True
                break

        if not out_of_range and not not_equal:
            #pp += [(i,j), (i+pair[0],j+pair[1]),(i+pair[0]*2,j+pair[1]*2),(i+pair[0]*2,j+pair[1]*2)]
            count += 1

    #print(i,j, count)
    return count 

def x_mas_count(i, j):
    arr = [[(-1, -1), (1,1)], [(-1, 1), (1, -1)]]

    for pair in arr:
        cell_x = (pair[0][0] + i, pair[0][1] + j)
        cell_y = (pair[1][0] + i, pair[1][1] + j)
        try:
            if cell_x[0] < 0 or cell_y[0] < 0 + cell_x[1] < 0 or cell_y[1] < 0:
                raise Exception("p")
            g =  [c[cell_x[0]][cell_x[1]] ,c[cell_y[0]][cell_y[1]]]
            if sorted(g) != ["M", "S"]:
                return False

        except:
            return False

    return True


output = 0
output2 = 0

for i in range(length):
    for j in range(length):
        if c[i][j] == "X":
            output += eight_direc_search(i,j)
        if c[i][j] == "A":
            output2 += x_mas_count(i, j)

print(output)
print(output2)
f = open("Day2\d2.txt", "r")

c = f.read().strip().split("\n")

safe_count = 0

for i in c:
    arr = [*map(int,i.split())]

    og_arr = arr[::]
    is_safe = False

    for k in range(len(og_arr)+1):
        if k == len(og_arr):
            arr = og_arr
        elif k == 0:
            arr = og_arr[1:]
        else:
            arr = og_arr[:k] + og_arr[k+1:]

        is_inc = False
        is_dec = False
        equal = False

        for j in range(0, len(arr)-1):
            a = arr[j]
            b = arr[j+1]
            if a > b:
                is_dec = True
                diff = abs(a-b)
                if diff > 3:
                    equal = True
                    break

            elif a < b:
                is_inc = True
                diff = abs(a-b)
                if diff > 3:
                    equal = True
                    break

            else:
                equal = True
                break

        is_safe = not equal and ((is_inc+is_dec)==1)
        #print(og_arr, arr, not equal, ((is_inc+is_dec)==1))
        if is_safe:
            break
    
    if is_safe:
        safe_count += 1
    else:
        #print(og_arr,"unsafe")
        pass

print(safe_count)
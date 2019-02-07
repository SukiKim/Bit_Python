def summary(*args):
    total = 0
    avg = 0
    result = []

    for i in args:
        total += i
        result.append(i)
    maxval = minval = result[0]

    for i in range(0,len(result)-1):
        if maxval < result[i+1]:
            maxval = result[i+1]

        if minval > result[i+1]:
            minval = result[i+1]

    avg = total / 5
    return total, maxval, minval, avg


total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)



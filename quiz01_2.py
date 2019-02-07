def quiz02_2():

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    slice = list[3:7]

    list.remove(4)
    list.remove(5)
    list.remove(6)
    slice.reverse()

    list.insert(4, slice[1])
    list.insert(5, slice[2])
    list.insert(6, slice[3])
    print(list)



quiz02_2()
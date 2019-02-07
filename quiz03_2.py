lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned=[]
for i in range(0, len(lst)):
    if type(lst[i]) == int:
        lst_cleaned.append(lst[i])
    elif type(lst[i]) == float:
        lst_cleaned.append(lst[i])
print(lst_cleaned)
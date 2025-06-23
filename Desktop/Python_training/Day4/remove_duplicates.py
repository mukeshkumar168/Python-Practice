
#  without order
def remove_duplicates(list1):
    
    return set(list1)


#  Maintain order
def remove_duplicates(list1):

    sets = set()
    res = []

    for i in list1:
        if i not in sets:
            sets.add(i)
            res.append(i)

    
    return res

list1 = [2, 2 , 5, 4, 9, 8, 8 ]
print(remove_duplicates(list1))
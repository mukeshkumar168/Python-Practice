def sorting(tuple1):
    """ Sorts the tuple by second item"""
    

    # Convert to list and sort by second item
    sorted_list = sorted(tuple1, key=lambda x: x[1])

    #  Convert back to tuple
    sorted_tuple = tuple(sorted_list)

    print("Sorted Tuple:", sorted_tuple)

tuple1 = (('a', 50), ('b', 23), ('c', 7), ('d', 35))
sorting(tuple1)
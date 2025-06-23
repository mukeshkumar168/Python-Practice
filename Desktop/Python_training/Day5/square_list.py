def square_list(list1):
    """ Squares the every value in the list
    Returns:
        list: Squared list
    """
    squared_list = [x**2 for x in list1]  # square the value 
    return squared_list

list1 = [2, 4, 6, 8, 10]
print(square_list(list1))
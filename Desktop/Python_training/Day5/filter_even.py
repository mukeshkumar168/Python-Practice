
def filter_even(list1):

    """filter the even number in list
    methods:
        even = > logic for even 
        Returns:
            bool: Even or not even"""

    def even(x):
        if x % 2 == 0:
            return True
        else:
            return False
        
    even_numbers = filter(even, list1)  # filter for map function to every numbers

    for i in even_numbers:
        print(i)


list1 = [7, 9, 2, 5, 6, 3, 1, 4, 8 ]
filter_even(list1)
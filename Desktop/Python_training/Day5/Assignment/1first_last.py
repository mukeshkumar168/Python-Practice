def first_last_swap(lst):

    """Interchange the first and last element
    returns:
        list: swapped list"""
    try:
        if not lst:    # Checks List is empty
            raise ValueError("List is empty.")
        
        if len(lst) < 2:    #Checks list has only one value
            print(" nothing to swap.")
            return lst

        # Swap the first and last elements
        lst[0], lst[-1] = lst[-1], lst[0]
        return lst

    except Exception as e:
        
        print(f"Error: {e}")
        return lst
    
# input
lst = [4, 5, 6]
print(first_last_swap(lst))
def find_largest(arr):
    """Finds Largest element in Array
       Returns:
            int: Largest element """

    try:

        if not arr:    # Checks array is empty
            raise ValueError("Array is empty")
        
        largest = arr[0]    # assuming first element as largest

        for i in arr:  
            if i>largest:   # checks others values greater than largest
                largest = i

        return f'Largest: {largest}'
    
    except Exception as e:

        return f'Error in Find_largest{e}'
    
arr = [50, 80, 90, 20, 10]
print(find_largest(arr))
def binary_search(sorted_list, target):
    """
        Function represents  the binary search.
        Returns:
            int : index position of item
    """

    low = 0   # initial 
    high = len(sorted_list)-1  # last

    while low<=high:    
        
        mid = (low +high)//2  # middle index 
        middle_v = sorted_list[mid]     #middle valuw

        if middle_v == target:      # comparing middle value as target 
            return f'Element at {mid}' 
        
        elif middle_v < target:   # middle value less than target

            low = mid + 1   # inital is change with mid + 1

        else:
            
            high = mid -1  # last is change with mid - 1

    return f'Not found' # not found

if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50, 60, 70]
    target = int(input("Enter number to search: "))
    print(binary_search(numbers, target))
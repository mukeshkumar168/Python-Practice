def find_pairs_with_sum_nested(arr, target_sum):
    """
    Find all unique pairs in the list
    """
    try:

        if not arr:
            raise ValueError("Array is empty.")

        pairs = []

        # takes one element
        for i in range(len(arr)):
            # takes next element
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target_sum:

                    # Sort the pair so that (2,7) and (7,2) are treated the same
                    pair = tuple(sorted((arr[i], arr[j])))

                    if pair not in pairs:  # Avoid duplicates
                        pairs.append(pair)
                        
        # Print the result
        if pairs:
            print(f"Unique pairs that sum to {target_sum}:")
            for p in pairs:
                print(p)
        else:
            print(f"No pairs found that sum to {target_sum}.")

    except Exception as e:
        print(f"Error: {e}")


arr = [2, 4, 3, 5, 7, 8, -1]
target = 9
find_pairs_with_sum_nested(arr, target)

def binary_search(arr, target):
    """
    Binary Search function that returns the index of the target if found,
    otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        
        # Debug: Uncomment the following line to see the current search bounds and mid value.
        # print(f"Searching between indexes {low} and {high}. Mid is {mid}.")

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Target is not present in the array

if __name__ == "__main__":
    # Example sorted list. Binary search requires the list to be sorted.
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # User input for the target value to search
    target_value = int(input("Enter the number to search: "))

    # Call binary_search function
    result = binary_search(sorted_list, target_value)

    # Output the result
    if result != -1:
        print(f"Found {target_value} at index {result}.")
    else:
        print(f"{target_value} is not in the list.")

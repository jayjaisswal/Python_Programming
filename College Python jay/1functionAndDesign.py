def isSorted(lst):
    # Check if the list is empty or contains only one element (both are considered sorted)
    if len(lst) <= 1:
        return True
    
    # Loop through the list and compare each element with the next one
    for i in range(len(lst) - 1):
        # If the current element is greater than the next element, return False
        if lst[i] > lst[i + 1]:
            return False
            
    # If the loop completes without finding any unsorted elements, return True
    return True

my_list = [1, 2, 3, 4, 5]
print(isSorted(my_list)) 

my_list = [1, 3, 2, 4, 5]
print(isSorted(my_list)) 


# A list is sorted in ascending order if it is empty or each item except the last one is less 
# than or equal to its successor. Define a predicate isSorted that expects a list as an 
# argument and returns True if the list is sorted, or returns False otherwise.
# (Hint: For a list of length 2 or greater, loop through the list and compare pairs of items, 
# from left to right, and return False if the first item in a pair is greater.)
def isSorted(lst):
    """Predicate to check if a list is sorted."""
    if len(lst) <= 1:
        return True  # An empty list or a list with one element is considered sorted
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Test the function with a list
test_list = [1, 2, 3, 4, 5]
print(isSorted(test_list))  

# Test with a non-sorted list
non_sorted_list = [5, 2, 8, 1, 6]
print(isSorted(non_sorted_list))  

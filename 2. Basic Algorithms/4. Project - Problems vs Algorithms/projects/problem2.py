def rotated_array_search(input_list, target_number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) <= 0:
        return 'Minimum length of the input list must be 1 !'
    if type(target_number) != int:
        return 'Target number type must be integer !'

    return recursive_search(input_list, target_number, 0, len(input_list)- 1)

def recursive_search(input_list, target_number, lower_boundary, upper_boundary):
    if lower_boundary > upper_boundary:
        return -1

    median_index = (lower_boundary + upper_boundary) // 2
    median_value = input_list[median_index]

    if median_value == target_number:
        return median_index
    
    left_side_index = recursive_search(input_list, target_number, lower_boundary, median_index - 1)
    right_side_index = recursive_search(input_list, target_number, median_index + 1, upper_boundary)
    
    return max(left_side_index, right_side_index)
 
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        
# Test Case 1 #######################################################
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print("TEST1_DONE\n")

# Test Case 2 #######################################################
print ("Pass" if ('Minimum length of the input list must be 1 !' == rotated_array_search([], 8)) else "Fail")
print("TEST2_DONE\n")

# Test Case 2 #######################################################
print ("Pass" if ('Target number type must be integer !' == rotated_array_search([6, 7, 8, 1, 2, 3, 4], '8')) else "Fail")
print("TEST3_DONE\n")
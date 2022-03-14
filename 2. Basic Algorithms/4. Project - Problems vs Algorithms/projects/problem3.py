def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if type(input_list) != list:
        return 'Input must be a list !'
    if len(input_list) <= 0:
        return 'Minimum input list length is 1 !'

    sorted_list = mergesort(input_list)
    number_one_list = [str(x) for x in sorted_list[0::2] if x >= 0]
    number_two_list = [str(x) for x in sorted_list[1::2] if x >= 0]

    return int(''.join(number_one_list)), int(''.join(number_two_list))

def mergesort(input_list):
    if len(input_list) <= 1:
        return input_list
    
    median_index = len(input_list) // 2
    left_list = mergesort(input_list[:median_index])
    right_list = mergesort(input_list[median_index:])

    return merge(left_list, right_list)

def merge(left_list, right_list):
    print(left_list, right_list)
    merged_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            merged_list.append(right_list[right_index])
            right_index += 1
        else:
            merged_list.append(left_list[left_index])
            left_index += 1

    merged_list += left_list[left_index:]
    merged_list += right_list[right_index:]

    return merged_list

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test Case 1 #######################################################
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
print("TEST1_DONE\n")

# Test Case 2 #######################################################
print ("Pass" if  ("Minimum input list length is 1 !" == rearrange_digits([])) else "Fail")
print("TEST2_DONE\n")

# Test Case 2 #######################################################
print ("Pass" if  ("Input must be a list !" == rearrange_digits((1,2,3,4))) else "Fail")
print("TEST3_DONE\n")
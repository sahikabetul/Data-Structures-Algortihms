import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if type(ints) != list:
        return 'Input must be a list !'
    if len(ints) <= 0:
        return 'Minimum input list length is 1 !'

    min_val = ints[0]
    max_val = ints[0]

    for int in ints:
        if int > max_val:
            max_val = int
        if int < min_val:
            min_val = int

    return (min_val, max_val)

# Test Case 1 #######################################################
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("TEST1_DONE\n")

# Test Case 2 #######################################################
l = []
get_min_max(l)
print ("Pass" if ('Minimum input list length is 1 !' == get_min_max(l)) else "Fail")
print("TEST2_DONE\n")

# Test Case 2 #######################################################
l = (1,2,3)
get_min_max(l)
print ("Pass" if ('Input must be a list !' == get_min_max(l)) else "Fail")
print("TEST3_DONE\n")
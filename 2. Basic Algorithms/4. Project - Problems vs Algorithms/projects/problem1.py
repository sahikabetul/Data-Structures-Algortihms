def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == None:
        return  "Enter a number !"
    if number < 0:
        return  "Minimum number is 0 !"
    
    lower_boundry = 1
    upper_boundry = number

    while lower_boundry <= upper_boundry:
        middle = int((lower_boundry + upper_boundry) / 2)
        middle_sq = middle ** 2

        if middle_sq == number:
            return middle
        elif middle_sq < number:
            lower_boundry = middle + 1
        else:
            upper_boundry = middle - 1

    return upper_boundry

# Test Case 1 #######################################################
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("TEST1_DONE\n")

# Test Case 2 #######################################################
print ("Pass" if  ("Minimum number is 0 !" == sqrt(-25)) else "Fail")
print("TEST2_DONE\n")

# Test Case 2 #######################################################
print ("Pass" if  ("Enter a number !" == sqrt(None)) else "Fail")
print("TEST3_DONE\n")
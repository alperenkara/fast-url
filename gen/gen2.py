# Palindrome detector

# user input-> 12345 
# computer input -> 54321 
# comparison 

def is_palindrome(num):
    # Skip if the number has single digit.
    
    if num // 10 == 0:
        return False
    
    # assign the input value onto temp variable
    temp = num 
    reversed_num = 0
    
    while temp != 0:
        print("Temp 1: ", temp)
        reversed_num = (reversed_num * 10) + (temp % 10)
        print("Reversed Num: ",reversed_num)
        print("Temp 2: ", temp)
        temp = temp // 10
        
    if num == reversed_num:
        return "{} is a palindrome".format(num)
    else:
        return "{} is NOT a palindrome".format(num)
        
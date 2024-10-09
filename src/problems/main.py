def check_duplicates_array(myArray: list):
    duplicate = set()

    for num in myArray:
        if myArray.count(num) > 1:
            duplicate.add(num)
        
    if len(duplicate) != 0:
        return True
    else:
        return False

print(check_duplicates_array([1, 2, 3, 1]))
print(check_duplicates_array([1, 2, 3, 4]))

def check_num_palindrome(number):
    palindrome = int(str(number)[::-1])

    if number == palindrome:
        return True
    else:
        return False

print(check_num_palindrome(12321))
print(check_num_palindrome(123))
def check_duplicates_array(myArray: list):
    duplicate = set()

    for num in myArray:
        if myArray.count(num) > 1:
            duplicate.add(num)
        
    if len(duplicate) != 0:
        return True
    else:
        return False

print(check_duplicates_array([1, 2, 3, 4]))
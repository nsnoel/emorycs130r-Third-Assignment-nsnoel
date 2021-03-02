'''
Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 


=================


1. string_max_length(strings_list) --> 30% 
Get a string list as input from the user and calculate the length of each string. Return the longest string. 
If multiple strings have same max value, return the first one.

------------------------------------------------

2. matrix_multiplication(matrix_1, matrix_2) --> 40%

----------------------------------------------------------------

3. working_numbers_set(input_list) --> 30% 
 
To the function, send an input list such that it has duplicates. Return a new list such that it has only unique elements from the list.

BONUS: If the function has only one line -- +20%

'''
#1

def string_max_length(strings_list):
    return max(strings_list, key=len)
   
if __name__ == "__main__":
    strings_list = list()
    print("Please enter strings for list with 4 values")
    for i in range(4):
        strings_list.append(input(f"Enter string value for index number {i} : "))
    print(f"The list is: {strings_list}")
    string_max_length(strings_list)
    a = string_max_length(strings_list)
    print(f"The longest string is: {a}")

#3

def working_number_set(input_list):
    return list(set(input_list))

if __name__ == "__main__":
    input_list = list()
    print("Enter list with duplicate values.")
    for i in range(5): 
        input_list.append(input(f"Enter value for index {i}: "))
    print(f"The list is: {input_list} ")
    result = working_number_set(input_list)
    print(f"The list without duplicate values is : {result}")


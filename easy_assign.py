'''
Implement the following functions based on the question. Retain the name of the functions, and parameters as is in the question. 

=================


1. construct_matrix(m, n) --> 30% 
Get the row and column of matrix, and return a Matrix with random float values.  

------------------------------------------------

2. return_below_n(input_list, value) --> 40%
 
Get an input list with random values, and a value from the user. Create another list with only values lesser than value and return it to the user. 

----------------------------------------------------------------

3. search_for_item(input_list, item) --> 30% 

Generate an input array and get an input for a number to search from the user. Return the index in which the item is found, or return -1 if not found. 


'''
#1
import random 

def construct_matrix(m,n):
    matrix = []
    for i in range(m): 
        temp_row = []
        for i in range(n):
            temp_row.append(random.uniform(0.1,24.5))
        matrix.append(temp_row)
    return matrix 

if __name__ == "__main__":
    m = int(input("Enter row for matrix: "))
    n = int(input("Enter column for matrix: "))
    result = construct_matrix(m,n)
    print(result)


#2
 
import random 

def return_below_n(input_list, value):
    first_list = []
    for i in input_list:
        if i < value:
            first_list.append(i)
    return first_list  

if __name__ == "__main__":
    value = int(input("Enter number under 100 to compare with list: "))
    input_list = [random.randrange(1,100,1) for i in range(5)] 
    print(f"The list your value will be compared to is: {input_list}")
    return_below_n(input_list, value) 
    a = return_below_n(input_list, value)
    print(f"The values in the list that are less than your inputted value are: {a}") 
     

#3

def search_for_item(input_list, item):
    result = -1
    if item in input_list:
        result = input_list.index(item)
    return result 

if __name__ == "__main__":
    input_list = []
    number = int(input("How many numbers in array? : "))
    for i in range(0, number): 
        input_list.append(int(input(f"Enter value for index {i}: ")))
    print(input_list)
    item = int(input("Enter number to search array for: "))
    print(f"The index for item is : {search_for_item(input_list, item)}")




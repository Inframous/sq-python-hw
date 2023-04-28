# Homework #2
#
# Create a list with your identification information.
# For example my lists length will be 4. If I will reach the value of the list on index 0, list[0] I will receive the “Alex”. Run with for loop over the list and print its content.

myList = ['SomeName', '(212)-555-5555', 'someone@somewhere.com', 'SomeCity']
print(myList[0])
for item in myList:
    print(item)

# Create a program that receives two lists of the same length with integers as values,
# if the lists are not of the same length the program must return the relevant error.
# The program will create a new list that will contain the largest value between the two lists at a specific index.
# Example:
# Input of two lists:

# output:
# [5, 4, 3, 4, 5]
# In the end of the program you must print the new list.

def its_war(lst1,lst2):
    mylist = []
    try:
        assert len(lst1) == len(lst2)
    except AssertionError:
        return "Lists are not of equal lengths."
    else:
        for num in lst1:
            if num >= lst2[lst1.index(num)]:
                mylist.append(num)
            else:
                mylist.append(lst2[lst1.index(num)])
        return mylist

lst1 = [1,2,3,4,5]
lst2 = [5,4,3,2,1]
print(its_war(lst1,lst2))
lst1 = [1,2,3,4,5,6]
lst2 = [5,4,3,2,1]
print(its_war(lst1,lst2))


# Create a python program that will count the number of appearances of odd and even values in a list.
# In case that the program encounters a string use break statement and return a print that says, “It’s a string!!!”
# and nullify the values of odd and even numbers counters.
# Example:
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
# list = [1, 2, 3, 4, “Oops”, 6, 7, 8, 9]
# Expected Output :
# “It’s a string!!!”

def check_odds_evens(mylist):
    odds = 0
    evens = 0
    for num in mylist:
        try:
            assert type(num) == int
        except AssertionError:
            return "It's a string!!!"
        else:
            if num % 2 == 0:
                odds += 1
            else:
                evens += 1
    return f"Number of even numbers: {evens}\nNumber of odd numbers: {odds}"

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myList2 = [1, 2, 3, 4, "Oops", 6, 7, 8, 9]
print(check_odds_evens(myList))
print(check_odds_evens(myList2))

# Build a function that will receive a list with integer values as its input.
# The function will calculate the sum of the integers in the list and will return the sum result.

def sum_list(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum
mylist = [1,2,3,4,5,6,7,8,9]
print(sum_list(mylist))


# Build a function that will receive a list with integer values as its input.
# The function will multiply all values in the list and return the result.


def multiply_list_items(lst):
    result = 1
    for i in lst:
        result *= i
    return result

mylist = [4,5,3]
print(multiply_list_items(mylist))


# Build a function that will receive a list with integer values as its input.
# The function will find the minimal value in the list and return this value.

def find_smallest_int(lst):
    current = lst[0]
    for num in lst:
        if num < current:
            current = num
    return current
mylist = [3, 4, 1, 7, 5, 2]
print(find_smallest_int(mylist))

# Build a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String: ‘Alex Kuznetsov’
# Expected Output:
# No. of Upper case characters: 2
# No. of Lower case Characters: 11

def find_caps(mystring):
    lowercase = 0
    uppercase = 0
    for i in mystring:
        if i == ' ':
            pass
        elif i.isupper():
            uppercase += 1
        else:
            lowercase +=1
    return f"No. of Upper case characters: {uppercase}\nNo. of Lower case characters: {lowercase}"

MyString = 'Alex Kuznetsov'
print(find_caps(MyString))





# Challenges:
# Build a Python function that takes a list and returns a new list with unique elements of the first list.
# Example:
# Input list : [1,2,3,3,3,3,4,5]
# Output list : [1, 2, 3, 4, 5]
def find_unique(lst):
    mylist = []
    for item in lst:
        if item not in mylist:
            mylist.append(item)
    return mylist
lst1 = [1,2,3,3,3,3,4,5]
print(find_unique(lst1))

#
# Write a Python program to construct the following pattern, using a nested loop.
# 	1
# 	12
# 	123
# 	1234
# 	12345
# 	123456
# 	1234567
# 	12345678
#
def pyramix(n):
    for i in range(1, n):      # outer loop for rows
        for j in range(1, i+1):    # inner loop for columns
            print(j, end='')    # print number and stay on the same line
        print()

pyramix(9)



# Write a Python program to print the following patterns:
#
#
#  ****
#  *
#  *
#   ***
#      *
#      *
#  ****

def give_me_five():
    for i in range(7):
        for j in range(4):
            if i == 0 or i == 6 or j == 0 and i < 4 or j == 3 and i >= 3:
                print("*", end="")
            else:
                print(" ", end="")
        print()

give_me_five()

# Homework #3
#
# Create a dictionary that will include your identification information. Use relevant keys for each field.
# Use the tuple key for relevant declarations.
# Example: {(name, Last_name):’Alex Kuznetsov’, ‘age’:27, ‘phone number’: 0527389001}

mydict = {(name, Last_name):’Nicolai Tesla’, ‘age’:27, ‘phone number’: '(212)-555-5555'}

# Build a function that will receive a list as an input,
# the function will replace the fifth index character with the character ‘@’
# if the fifth index doesn’t exist in the list please return a relevant exception.
# If there is no exception please return the updated list.

def replace_fifth(inputList):
    try:
        inputList[5] = "@"
        return inputList
    except IndexError:
        return "There is no 5th item to this list"

mylist = [1,2,3,4,5,6,7]
print(replace_fifth(mylist))
print("")
mylist = [1,2,3]
print(replace_fifth(mylist))

# Build a function that will receive a list as an input,
# the function will replace the fifth index character with the character ‘@’
# if the fifth index doesn’t exist in the list please return a relevant assertion.
# If there is no assertion please return the updated list.

def replace_fifth_assert(mylist):
    try:
        assert mylist[5]
        mylist[5] = "@"
        return mylist
    except IndexError:
        return "There is no fifth index to this list."

mylist = [1,2,3,4,5,6,7]
print(replace_fifth_assert(mylist))
print("")
mylist = [1,2,3]
print(replace_fifth_assert(mylist))

# Build a function that will receive a dictionary a new key and a new key value.
# The function will add the new key value to the dictionary and will return the updated dictionary.
# Solution:

def add_item_to_dict(dictInput, key, value):
    dictInput[key] = value
    return dictInput

mydict = { 'Apple': 'MacOS', 'PC': 'Windows'}
print(add_item_to_dict(mydict, 'iPhone', 'iOS'))


# Write a Python script to generate and print a dictionary
# that contains a number (between 1 and n) in the form (x, x+3).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 4, 2: 5, 3: 6, 4: 7, 5: 8}
# Solution:
def my_dict_gen(n):
    mydict = {}
    for i in range(1,n+1):
        mydict[i] = i + 3
    return mydict

print(my_dict_gen(5))


# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict4 = {**dic1, **dic2, **dic3}
print(dict4)


# Build a function that will count appearances of each character in the string and will
# return a dictionary with string characters as keys and the frequency of each character as key value.
# Example:
# Input string : 'HANNA’
# Expected output: {‘H’: 1, ‘A’: 2, ‘N’: 2}

def char_cout(mystring):
    count = {}
    for char in mystring:
        if char.capitalize() in count.keys():
            count[char.capitalize()] += 1
        else:
            count[char.capitalize()] = 1
    return count

mystring = "Banana"
print(char_cout(mystring))

# Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
def dict_combiner(d1,d2):
    mydict = {}
    for key in d1.keys():
        if key in d2.keys():
            mydict[key] = d1[key] + d2[key]
        else:
            mydict[key] = d1[key]
        for key in d2.keys():
            if key not in mydict.keys():
                mydict[key] = d2[key]
    return mydict

print(dict_combiner(d1,d2))

# Challenges:
#
#
# Build a Python function to calculate the factorial of a number (a positive integer).
# The function accepts the number as an argument. Please use recursion.
# In case that your input is negative integer please return an assertion.
def fact(n):
    try:
        assert n >= 0
    except AssertionError:
        return "Number MUST be a positive integer."
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
print(fact(-5))

# Create a recursive function to calculate the sum of the positive integers of n+ (n-1) + (n-3)... (Until n-x <= 0).
# The n value is the function input the summary result is the output of the function.

### I didn't understand this question. <---------- NOTE!


# Create a recursive function to calculate the value of 'a' to the power 'b'.
# Example power (3, 2) This means that we are calculating the result of 32=9.

def i_got_the_power(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return i_got_the_power(a, b // 2) ** 2
    else:
        return a * i_got_the_power(a, b - 1)

print(i_got_the_power(4,2))

# Homework #1 

# Create a program that will print your identifications.
# Example my identifications:
# Name: Alex
# Last name: Kuznetsov
# Age: 27 
# Phone number: 0527389001

print("""
Fist Name: Danny
Last Name: Kay
Age: 47
Phone Number: (212) 555 1234
""")

# For a string that you created please check if:
# The character at index 7 equals ‘a’.
# The character at index 8 equals ‘b’.
# The character at index 9 equals ‘c’.
# If all conditions exists please print “True”,
# Else print False.
# Pay attention for edge cases like the length of the string and so on.
# Your program must not crash for any string.  
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


def checkStuff(stuff):
    try:
        assert len(stuff) >= 8
    except AssertionError:
        pass
    if stuff[6] == 'a' and stuff[7] == 'b' and  stuff[8] == 'c':
        return "True!!"
    else:
        return "False!!"

my_string = "This is my string!"
my_2nd_string = "type zabc"
print(checkStuff(my_string))
print(checkStuff(my_2nd_string))



# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.

def addingly(stuff):
    if len(stuff) < 3:
        pass
    else:
        if stuff.endswith('ing'):
            stuff = stuff + 'ly'
        else:
            stuff = stuff + 'ing'
        
    return stuff

print(addingly('deal'))
print(addingly('seaming'))
print(addingly('to'))




# For a string (three characters and more) that you have created 
# please create a new string that follows the next rules:
# The first character of the new string is the middle character of the original string. 
# The middle character of the new string is the last character of the original string. 
# The last character of the new string is the first character of the original string.
# Example:
# For odd length case, length of 9 characters:
# Let’s assume that the middle character is 9/2 rounded down that’s means that it is 4.
# “afffbeeec” –> “bfffceeea”
# For even length case, length of 8 characters:
# The middle character is also 4 because 8/2 equals 4.
# “axxxbyyc” -> “bxxxcyya”
# 	Print your new string in the following way, for even length example:
# 	The rotated string is bxxxcyya

def switcharoo(stuff):
    length = len(stuff)
    mid = length // 2
    new_str = stuff[mid] + stuff[:mid][::-1] + stuff[length-1:mid:-1] + stuff[0]
    return f"The rotated string is {new_str}"

print(switcharoo('afffbeeec'))
print(switcharoo('axxxbyyc'))

# Write a Python function to insert a string in the space of the original string.
# You can assume that there is just one space in your string. 

def insert_in_space(stuff, newWord):
    stuff = stuff.split(' ')
    stuff.insert(1, newWord)
    return ' '.join(stuff)

print(insert_in_space('Hello World!', 'New'))



# Challenges: 
# Write a Python program to sort a string lexicographically. Look For relevant method. 

def sort_lex(stuff):
    stuff = list(stuff)
    stuff.sort()
    return ''.join(stuff)

print(sort_lex('qwertyuiopasdfghjklzxcvbnm)(*&^%$#@!)'))



# Write a Python program to print the following floating numbers upto 2 decimal places.

## I didn't understand the task <<------ 

# Write a Python program to count occurrences of a substring in a string. Look for a relevant method. 

def find_string(substring, mystring):
    mystring = mystring.lower()
    substring = substring.lower()
    count = mystring.count(substring)
    return f'The string "{substring}" appears {count} times in the string'

my_song = """You say yes, I say no
You say stop and I say go, go, go
Oh, no
You say goodbye and I say hello
Hello, hello
I don't know why you say goodbye
I say hello
Hello, hello
I don't know why you say goodbye
I say hello"""


print(find_string('hello', my_song))

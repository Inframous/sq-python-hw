def add_int(a,b):
    return a + b

def multiply_int(a,b):
    return a * b

def divide_int(a,b):
    if b == 0: 
        raise ValueError
    return a / b

def check_palindrome(text):
    original_text = text
    test_text = text[::-1]
    for letter in range(0, len(original_text)):
        if original_text[letter] != test_text[letter]:
            return False
    return True

def reverse_string(text):
    return text[::-1]





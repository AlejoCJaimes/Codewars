# Write a function named first_non_repeating_letter that takes a string input, 
#and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', 
#since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, 
#but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


def first_non_repeating_letter(string):
    """
    Logic code:
    1. read input and determinate if the input lenght is > 1.
    2. normalize string, using the method casefold and replace white spaces for nothing. (like be using trim)
    3. count all cases when a char into string is repeat twice or more times.
    4. Return the first output from the list when the position is one, because is the first element that only repeats one time.
    5. Remember the rules, if the string contains all elements the same character, returns '' or None for myself I'll go return ''
    6. The case sensitive for a string, you can convert to lower or upper for solve the problem, but at the end you need return the char like was the original.
    """
    if len(string) == 1:
        return string
    else:
        aux_str = string.replace(" ","").casefold() # normalize
        unique_dict = {char:aux_str.count(char) for char in aux_str}
        found_element = [k for k,v in unique_dict.items() if v==1]
        element = ''
        if len(found_element)>0:
            if string.find(found_element[0]) == -1:
                element = found_element[0].upper() 
            else:
                element = found_element[0] 
        else:
            pass
        return element
      
# Test Cases
# string = "Go hang a salami, I\'m a lasagna hog!"
# string1 = 'hello world, eh?'
# string2 = 'sTress'
# string3 = 'aabb'
# string4 = "f UoJeaBWS:GefxN1V9tUR98t;yIk"
# string6 = "6aMjSk,1 4ShyC0AJJfZXBV;;SkJrE.4Sgw4 UvimYR"
# print(first_non_repeating_letter(string6))

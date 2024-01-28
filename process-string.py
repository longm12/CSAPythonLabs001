# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyz"
user_range = input("Enter a range of letters (e.g., a-z): ")

<<<<<<< HEAD
def repeat_chars(string):
    result = ""
    for char in string:
        result += char * 2
    return result
print(repeat_chars("String"))      # Output: "SSttrriinngg"
print(repeat_chars("Hello World")) # Output: "HHeelllloo WWoorrlldd"
print(repeat_chars("1234!_ "))     # Output: "11223344!!__ "
=======

>>>>>>> 93130f284b9994d68d12d0ad5fe4c1726a826dbe

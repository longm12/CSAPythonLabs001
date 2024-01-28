# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Exaples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "


# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Exaples
# "a-z" ➞ "abcdefghijklnopqrstuvwxyz"
# "h-o" ➞ "hijklno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklnopqrstuvwxyz"
user_range = input("Enter a range of letters (e.g., a-z): ")


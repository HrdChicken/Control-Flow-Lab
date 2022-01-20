# exercise-01 Vowel or Consonant
# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
alphabet = input('Please enter a letter from the alphabet (a-z or A-Z): \n')

# 2. Write the code that determines whether the letter entered is a vowel
if alphabet in ('a','e','i','o','u','A','E','I','O','U'):

# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
    print('is a vowel')
else:
    print('is a constant')

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
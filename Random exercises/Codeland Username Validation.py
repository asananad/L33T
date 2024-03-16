"""
Codeland Username Validation
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
"""


def CodelandUsernameValidation(strParam):

  # code goes here
  lenght = len(strParam)
  if lenght < 4 or lenght > 25 or strParam[0].isalpha() != True or strParam[0] == "_":
    strParam = "False"
  else:
    allowed_chars = set(
    ("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"))
    if set((strParam)).issubset(allowed_chars) == False:
      strParam = "False"

  if strParam != "False": strParam = "True"

  return strParam

# keep this function call here 
print(CodelandUsernameValidation(input()))
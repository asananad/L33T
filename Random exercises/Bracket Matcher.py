#Bracket Matcher

"""
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.
Examples
Input: "(coder)(byte))"
Output: 0
Input: "(c(oder)) b(yte)"
Output: 1
"""

def BracketMatcher(strParam):

  # code goes here
  open_brackets = 0
  close_brackets = 0

  for x in strParam:
    if x == "(":
      open_brackets += 1
    elif x == ")":
      close_brackets += 1


  if open_brackets == close_brackets:
    return 1
  else:
    return 0

# keep this function call here 
print(BracketMatcher(input()))
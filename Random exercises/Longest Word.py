# Longest Word
"""
Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
Examples
Input: "fun&!! time"
Output: time
Input: "I love dogs"
Output: love
"""

import re

def LongestWord(sen):

  list1 = re.findall("[a-zA-Z0-9]+", sen)
  lenght_list = []
  for x in list1:
    lenght_list.append(len(x))
  return list1[lenght_list.index(max(lenght_list))]

# keep this function call here 
print(LongestWord(input()))
# Capitalize the first letter of every word in a given string

string = "the quick brown fox jumps over the lazy dog."
WIP_string = ""
for x in string.split():
  cap_word = x[0].upper()
  counter = 1
  while counter <= (len(x) - 1):
    cap_word += x[counter]
    counter += 1
  WIP_string += cap_word + " "

final_string = WIP_string[:-1]
print(final_string)
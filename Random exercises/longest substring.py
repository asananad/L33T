# Get longest substring of unique characters

input = "4thequickbrownfoxjumpsoverthelazydog"

substring_list = []
char_list = []

i = 0

while i < len(input):
  if input[i] not in char_list:
    char_list.append(input[i])
    i += 1
  else:
    substring_list.append(char_list)
    char_list = []
    i = input.rfind(input[i], 0, i - 1) + 1
substring_list.append(char_list)

list_lenghts = []

for list in substring_list:
  list_lenghts.append(len(list))

print("".join(substring_list[list_lenghts.index(max(list_lenghts))]))
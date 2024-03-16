# Check if palindrome

input = "tacocat"
left_index = 0
right_index = -1

for x in range(len(input) // 2):
  if input[left_index] != input[right_index]:
    print("Not a palindrome")
    quit()
  else:
    left_index += 1
    right_index -= 1
print("It's a palindrome")

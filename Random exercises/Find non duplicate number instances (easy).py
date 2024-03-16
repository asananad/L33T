# Find Non-Duplicate Number Instances (easy)

"""
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The relative order of the elements should be kept the same and you should not use any extra space so that the solution has constant space complexity i.e., .

Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after moving element will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after moving elements will be [2, 11].
"""

input = [2, 2, 2, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]

def do_thing(input):
  last_unique_i = 0
  for x in range(len(input)):
    current = input[x]
    if input.count(input[x]) == 1:
      input.pop(x)
      input.insert(last_unique_i, current)
      last_unique_i += 1
    else:
      already_moved = False
      for y in range(0, last_unique_i):
        if current == input[y]:
          already_moved = True
      if already_moved is False:
        input.pop(x)
        input.insert(last_unique_i, current)
        last_unique_i += 1
  return last_unique_i

print(do_thing(input))
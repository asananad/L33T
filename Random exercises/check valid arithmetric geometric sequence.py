# Check if valid arithmetric or geometric sequence.

def check(il):
  arithmetic_diff = il[1] - il[0]
  arith_validity = True
  for x in range(len(il) - 1):
    if il[x + 1] - il[x] != arithmetic_diff:
      print("Invalid arithmetic sequence")
      arith_validity = False
      break

  if arith_validity:
    print("Valid arithmetic sequence")
  else:
    geometric_diff = il[1] / il[0]
    geometric_validity = True
    for x in range(len(il) - 1):
      if il[x + 1] / il[x] != geometric_diff:
        print("Invalid geometric sequence")
        geometric_validity = False
        break
    if geometric_validity:
      print("Valid geometric sequence")


#Valid arithmetic: [5, 7, 9, 11, 13, 15, 17]
#Valid geometric: [2, 6, 18, 54, 162, 486, 1458]

il = [5, 7, 9, 11, 13, 15, 17]
check(il)

# First factorial

def FirstFactorial(num):

  result = 1
  for x in range(1, num + 1):
    result = result * x
  return result

# keep this function call here 
print(FirstFactorial(input()))
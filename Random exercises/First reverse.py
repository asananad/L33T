# First reverse

def FirstReverse(strParam):

  str_list = []
  for x in strParam:
    str_list.insert(0, x)
  
  strParam = "".join(str_list)

  return strParam

# keep this function call here 
print(FirstReverse(input()))
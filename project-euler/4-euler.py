#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

maxnum = 999
numbers_array = []
while maxnum > 1:
    num = 999
    while num > 1:
        current = str(num * maxnum)
        if len(current) > 5:
            if current[0] == current[-1] and current[1] == current[-2] and current[2] == current[-3]:
                current = int(current)
                numbers_array.append(current)
                break
        num = num - 1
    maxnum = maxnum - 1
print(max(numbers_array))
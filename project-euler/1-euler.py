#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

num = 1
num_array = []
while num < 1000:
    if num/3 == num//3:
        num_array.append(num)
        num = num + 1
    else:
        if num/5 == num//5:
            num_array.append(num)
            num = num + 1
        else:
            num = num + 1
print(sum(num_array))
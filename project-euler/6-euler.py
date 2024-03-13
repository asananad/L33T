#The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10^2) = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

i = 1
number_list = []
while i <= 100:
    number_list.append(i * i)
    i = i + 1
sum_of_squares = sum(number_list)

i = 1
number_list2 = []
while i <= 100:
    number_list2.append(i)
    i = i + 1
square_of_sum = sum(number_list2) * sum(number_list2)

print(square_of_sum - sum_of_squares)
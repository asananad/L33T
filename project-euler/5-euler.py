#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 2520
i = 2
while i <= 20:
    if number / i == number // i:
        if i == 20:
            print(number)
            quit()
        i = i + 1
    else:
        number = number + 2520
        i = 2
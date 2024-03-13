#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

prime_number_list = []
number = 2
i = 2
while len(prime_number_list) != 10000:
    if number / i == number // i:
        number = number + 1
        i = 2
        continue
    else:
        if i == number - 1:
            prime_number_list.append(number)
        i = i + 1
print(prime_number_list[-1])
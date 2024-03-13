"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

all_numbers_list = []
for x in range(2, 2000000):
    all_numbers_list.append(x)
i = 0
e = 2.0
e2 = 2
while i <= 1999997:
    while e < 2000000 ** 0.5:
        if (all_numbers_list[i] * e) == (all_numbers_list[i] * e2):
            if all_numbers_list[i] * e2 in all_numbers_list:
                del all_numbers_list[all_numbers_list.index(all_numbers_list[i])]
                print("deleted " + str(all_numbers_list.index(i)))
                e = 2.0
                e2 = 2
                break
        e = e + 1
        e2 = e2 + 1
    i = i + 1
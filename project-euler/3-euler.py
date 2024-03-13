#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

target = 600851475143
counter = 2
while True:
    if target / counter == target // counter:
        factor = int(target / counter)
        counter2 = 2
        for x in range(factor - 2):
            if factor / counter2 == factor // counter2:
                break
            if counter2 == factor - 2:
                print(factor)
                quit()
            counter2 = counter2 + 1
    counter = counter + 1
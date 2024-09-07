from random import random, randint

counter = 1
while True:                             #create integer variable
    random_number = randint(1, 6)
    print("roll:", counter, "value:", random_number)
    if random_number == 1:                #if random number equals 1
        break                             #break out of loop
    counter += 1                          #increase counter
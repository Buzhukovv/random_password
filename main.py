def listToString(s):
    str1 = ""
    return (str1.join(s))

import random

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_list = []
for i in range(0, nr_letters):
    HighNumberAscii = random.randint(65, 90)
    LowNumberAscii = random.randint(97, 122)
    letterRand = random.randint(1,2)
    if letterRand == 1:
        asc = chr(HighNumberAscii)
        pass_list.append(asc)
    else:
        asc = chr(LowNumberAscii)
        pass_list.append(asc)
for i in range (0, nr_symbols):
    pass_list.append(random.choice(symbols))
for i in range (0, nr_numbers):
    pass_list.append(random.choice(numbers))
random.shuffle(pass_list)
print(listToString(pass_list))

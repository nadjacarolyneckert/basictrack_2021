numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]


for number in numbers:
    print(number)
    print(number, number**2)


total = 0
product = 1

for number in numbers:
    total += number
    print("The sum of the numbers is", total)
    product*=number
    print("The product of the numbers is", product)


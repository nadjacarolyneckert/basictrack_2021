numbers = [5, 15, 30, 27, 101, 99, 12, 27, 24, 66]

sum_even =0
for number in numbers:
    if number%2 == 0:
        sum_even += number

print("The sum of even numbers in our sample is ", sum_even)

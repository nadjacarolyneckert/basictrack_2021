numbers = [5, 15, 30, 27, 101, 99, 12, 27, 24, 66]

sum_uneven =0
for number in numbers:
    if number%2 != 0:
        sum_uneven += number

print("The sum of uneven numbers in our sample is ", sum_uneven)
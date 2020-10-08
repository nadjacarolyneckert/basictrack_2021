numbers = [5, 15, 30, 27, 101, 99, 12, 27, 24, 66]

count_uneven =0
for number in numbers:
    if number%2 !=0:
        count_uneven +=1

print("The amount of uneven numbers in our sample is ", count_uneven)
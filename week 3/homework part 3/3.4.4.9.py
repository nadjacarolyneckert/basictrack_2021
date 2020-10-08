n = 11

for divisor in range(2, n):
    if n % divisor == 0:
        print("False")
        break
else:
    print("True")

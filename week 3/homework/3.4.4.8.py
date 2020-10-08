side_a = 2
side_b = 4
side_c = 5
epsilon = 1e-7

sum_squares = (side_a ** 2) + (side_b ** 2)
hypotenues_square = side_c ** 2

if abs(sum_squares - hypotenues_square) < epsilon:
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")
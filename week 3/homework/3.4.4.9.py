
side_a = 4
side_b = 8
side_c = 6
epsilon = 1e-7

if side_a > side_c:
    side_a, side_c = side_c, side_a

if side_b > side_c:
    side_b, side_c = side_c, side_b

sum_of_squares = (side_a ** 2) + (side_b ** 2)
hypo_square = side_c ** 2

if abs(sum_of_squares - hypo_square) < epsilon:
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")

